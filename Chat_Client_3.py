import socket
import threading

HOST = '139.147.238.181' # replace with the IP address of the server
PORT = 5556 # replace with the port number of the server

nickname = input("Enter your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            print(msg)
        except:
            # an error occurred, probably the server has disconnected
            client.close()
            break

def write():
    while True:
        msg = f"{nickname}: {input()}"
        client.send(msg.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
