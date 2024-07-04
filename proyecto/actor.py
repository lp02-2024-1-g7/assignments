# proyecto\actor.py
import socket
import threading
import time

class Actor:
    def __init__(self, id, port):
        self.id = id
        self.port = port
        self.inbox = []  # Incoming messages

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

    def send(self, recipient, message):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # extract the recipient address and port
                host, port = recipient.split(':')
                s.connect((host, int(port)))
                s.sendall(message.content.encode())  # Convert the message content to bytes
        except Exception as e:
            print(f"Error sending message from Actor {self.id}: {e}")

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', int(self.port)))
            s.listen()
            print(f"Actor {self.id} listening on port {self.port}")
            while True:
                conn, addr = s.accept()
                threading.Thread(target=self.handle_connection, args=(conn,)).start()

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

class Message:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content
