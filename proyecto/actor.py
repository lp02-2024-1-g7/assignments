# proyecto/actor.py
import socket
import threading
import time

class Actor:
    def __init__(self, id, port):
        self.id = id
        self.port = port
        self.inbox = []  # Incoming messages
       

    def send(self, host, port, message):
        try:
            print(f"Attempting to send message to {host}:{port}")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, int(port)))
                print('Connection established')
                print(host, port, message)
                s.sendall(message.encode())  # Convert the message content to bytes
                print('Message sent')
        except Exception as e:
            print(f"Error sending message from Actor {self.id}: {e}")


    def start(self):
        threading.Thread(target=self.listen_for_messages).start()
        threading.Thread(target=self.listen_for_user_input).start()

    def listen_for_messages(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', int(self.port)))
            s.listen()
            print(f"Actor {self.id} listening on port {self.port}")
            while True:
                conn, addr = s.accept()
                threading.Thread(target=self.handle_connection, args=(conn,)).start()

    def listen_for_user_input(self):
        while True:
            user_input = input(f"Actor {self.id}> ")
            self.handle_user_input(user_input)

    def handle_user_input(self, user_input):
        parts = user_input.split(' ')
        command = parts[0]

        if command == "invoke":
            if len(parts) < 3:
                print("Usage: invoke <method_name> [params...]")
                return
            _, method_name, *params = parts
            if not hasattr(self, method_name):
                print(f"Actor {self.id} does not have a method named {method_name}.")
                return
            
            method = getattr(self, method_name)
            if method_name == "send": 
                host, port, *message= params
                sendable = ''
                for word in message:
                    sendable+=' ' + word
                method(host, port, sendable)
            
        else:
            print("Invalid command. Use 'send <message> <actor_id> to <address:port>' or 'invoke <actor_id> <method_name> [params]'.")

    def handle_connection(self, conn):
        with conn:
            data = conn.recv(1024)
            message = Message(data.decode('utf-8'))
            self.inbox.append(message)
            print(f"Actor {self.id} received: {message}")

    def print_inbox(self):
        print(f"Inbox of Actor {self.id}:")
        for message in self.inbox:
            print(message)

class Message:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content
