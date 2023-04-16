import socket
import random

MIN = 0
MAX = 100

PORT = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(("127.0.0.1", PORT))
    curr = random.randint(MIN, MAX)
    while True:
        mes = f"GUESS {curr}"
        print("Sending " + mes)
        sock.send(mes.encode())
        resp = sock.recv(1024).decode()
        print(f"Response {resp}")
        if (resp == "LESS"):
            curr = curr - 1
        elif (resp == "MORE"):
            curr = curr + 1
        elif (resp == "EQUAL"):
            print("Correct guess!")
            print(f"The answer is {curr}")
            break
        else:
            print(f"Bad response: {resp}")
            break
finally:
    sock.close()
    print("Cleint stoped")