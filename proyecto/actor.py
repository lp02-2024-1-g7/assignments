# proyecto/actor.py
import socket
import threading
import time

class Actor:
    actor_registry = {}  # Class-level registry for all actors

    def __init__(self, id, port):
        self.id = id
        self.port = port
        self.inbox = []  # Incoming messages
        Actor.actor_registry[id] = self  # Register the actor

    def send_broadcast(self, message):
        for port in range(9090, 9100):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1)  # Set a timeout for the connection attempt
                    s.connect(('localhost', port))
                    s.sendall(message.encode())
                    print(f"{self.id} sent broadcast: {message} to port {port}")
                    
                    # Wait for acknowledgment
                    ack_data = s.recv(1024)
                    if ack_data:
                        ack_message = ack_data.decode('utf-8')
                        print(f"Actor {self.id} received acknowledgment from port {port}: {ack_message}")
            except (socket.timeout, ConnectionRefusedError):
                print(f"Actor {self.id} did not find actor on port {port}")
            except Exception as e:
                print(f"Error sending broadcast message from Actor {self.id} to port {port}: {e}")
    def send(self, host, port, message):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # host, port = recipient.split(':')
                s.connect((host, int(port)))
                s.sendall(message.content.encode())  # Convert the message content to bytes
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
        if user_input.startswith("send "):
            parts = user_input.split(' ')
            recipient_id = parts[1]
            recipient = Actor.actor_registry.get(recipient_id)
            if recipient:
                recipient_port = recipient.port
                message_content = ' '.join(parts[2:])
                self.send(f"127.0.0.1:{recipient_port}", Message(message_content))
            else:
                print(f"Actor {recipient_id} not found.")
        elif user_input.startswith("invoke "):
            parts = user_input.split(' ')
            actor_id = parts[1]
            method_name = parts[2]
            args = parts[3:]  # Capture all remaining parts as arguments
            if actor_id in Actor.actor_registry:
                actor = Actor.actor_registry[actor_id]
                if hasattr(actor, method_name):
                    method = getattr(actor, method_name)
                    method(*args)  # Pass arguments to the method
                else:
                    print(f"Actor {actor_id} does not have a method named {method_name}.")
            else:
                print(f"Actor {actor_id} not found.")
        else:
            print("Invalid command. Use 'send <recipient_id> <message>' or 'invoke <actor_id> <method_name> [args...]'.")

    def handle_connection(self, conn):
        with conn:
            data = conn.recv(1024)
            message = Message(data.decode('utf-8'))
            self.inbox.append(message)
            print(f"Actor {self.id} received: {message}")

            # If the message is about a new actor being created, send an acknowledge
            if message.content == "new_actor_created":
                acknowledge_message = Message(f"{self.id} acknowledges new actor")
                conn.sendall(acknowledge_message.content.encode())
            elif "acknowledges new actor" in message.content:
                print(f"Actor {self.id} received acknowledgment: {message}")

    def print_inbox(self):
        print(f"Inbox of Actor {self.id}:")
        for message in self.inbox:
            print(message)

    def custom_method(self, *args):
        print(f"Custom method executed in Actor {self.id} with arguments: {args}")

class Message:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content
