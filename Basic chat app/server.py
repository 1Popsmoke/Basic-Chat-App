import socket
import threading

# List to keep track of connected clients
clients = []

# Broadcast function to send messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

# Handle client connection
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)  # Buffer size of 1024 bytes
            if not message:
                break
            print(f"Received: {message.decode('utf-8')}")
            broadcast(message, client_socket)  # Broadcast the message to other clients
        except:
            break

    # Remove client when they disconnect
    clients.remove(client_socket)
    client_socket.close()

# Set up the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))  # Listen on localhost and port 5555
    server.listen()

    print("Server is listening on port 5555...")
    
    while True:
        client_socket, client_address = server.accept()  # Accept new clients
        print(f"New connection from {client_address}")
        clients.append(client_socket)

        # Start a new thread to handle each client
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
