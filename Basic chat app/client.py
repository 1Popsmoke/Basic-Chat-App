import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            print(f"\n{message.decode('utf-8')}")
        except:
            print("Disconnected from server")
            break

# Connect to the server
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))  # Connect to the server on localhost and port 5555

    # Start a thread to listen for incoming messages
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    # Send messages to the server
    while True:
        message = input()
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
