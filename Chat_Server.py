import socket
import threading

HOST = 'localhost'  # server hostname or IP address
PORT = 8000  # server port number

clients = []  # list of connected clients

def broadcast(message):
    """Send a message to all connected clients"""
    for client in clients:
        client.send(message)

def handle_client(client_socket, client_address):
    """Handle a client connection"""
    print(f'New connection from {client_address}')
    clients.append(client_socket)
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                broadcast(message)
            else:
                remove(client_socket)
        except:
            remove(client_socket)
            break

def remove(client_socket):
    """Remove a client from the list of connected clients"""
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()

# create a TCP socket and bind it to the server address
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# listen for incoming connections
server_socket.listen()

print(f'Server listening on {HOST}:{PORT}')

# accept new connections and start a new thread for each client
while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
