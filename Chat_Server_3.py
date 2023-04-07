import socket
import threading

HOST = '0.0.0.0' # listen on all available interfaces
PORT = 5556 # choose a port number

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(msg):
    for client in clients:
        client.send(msg.encode())

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg:
                broadcast(msg)
            else:
                # client has disconnected
                clients.remove(client)
                client.close()
                break
        except:
            # client has disconnected
            clients.remove(client)
            client.close()
            break

while True:
    client, addr = server.accept()
    clients.append(client)
    print(f"Connected with {addr}")
    threading.Thread(target=handle_client, args=(client,)).start()
