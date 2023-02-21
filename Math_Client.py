import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 8081        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        problem = input("Enter a math problem to solve (or 'exit' to quit): ")
        if problem.lower() == "exit":
            break
        s.sendall(problem.encode())
        data = s.recv(1024)
        print(f"Answer: {data.decode()}")
