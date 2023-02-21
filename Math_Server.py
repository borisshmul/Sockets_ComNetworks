import socket
import re


def solve_math_string(math_string):
    # Use regular expressions to extract the numbers and operators from the string
    numbers = re.findall(r'\d+', math_string)
    operators = re.findall(r'[+*/\-]+', math_string)

    # Convert the numbers to floats
    numbers = [float(num) for num in numbers]

    # Use the operators to evaluate the expression
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i+1]
        elif operators[i] == '-':
            result -= numbers[i+1]
        elif operators[i] == '*':
            result *= numbers[i+1]
        elif operators[i] == '/':
            result /= numbers[i+1]

    return result
HOST = ''  # all available interfaces
PORT = 8081  # arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Server is listening on port {PORT}...")

    while True:
        conn, addr = s.accept()
        print(f"Connection from {addr} has been established.")

        data = conn.recv(1024)
        problem = data.decode()
        print(f"Received problem: {problem}")
        try:
            answer = str(solve_math_string(problem))
        except:
            answer = "Invalid expression"
        print(f"Sending answer: {answer}")
        conn.sendall(answer.encode())
        conn.close()
