import socket
import threading

HOST = 'localhost'  # server hostname or IP address
PORT = 8000  # server port number

# create a TCP socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive():
    """Receive and print messages from the server"""
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            # an error occurred, close the connection and exit
            client_socket.close()
            break

def send():
    """Send messages to the server"""
    while True:
        message = input()
        client_socket.send(message.encode())

# start two threads, one for sending messages and one for receiving messages
receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)
receive_thread.start()
send_thread.start()
