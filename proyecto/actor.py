# proyecto\actor.py
import socket
import threading
import time

class Actor:
    def __init__(self, id, port):
        self.id = id
        self.port = port
        self.actors = [] #Actores conocidos
        self.inbox = []  # Incoming messages

    def send(self, address, port, message):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # extract the recipient address and port
                s.connect((address, int(port)))
                s.sendall(message.content.encode())  # Convert the message content to bytes
        except Exception as e:
            print(f"Error sending message from Actor {self.id}: {e}")

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', int(self.port)))
            s.listen()
            print(f"{self.id} listening on port {self.port}")
            while True:
                conn, addr = s.accept()
                threading.Thread(target=self.handle_connection, args=(conn,)).start()

    def handle_connection(self, conn):
        with conn:
            data = conn.recv(1024)
            message = Message(data.decode('utf-8'))
            self.inbox.append(message)
            print(f"Actor {self.id} received: {message}")

class Message:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content
