import socket
import random

MIN = 0
MAX = 100

PORT = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.bind(('localhost', PORT))
    sock.listen()
    while True:
        hidden = random.randint(MIN, MAX)
        print("Waiting for connection")
        print(f"Hidden value: {hidden}")

        (conn, addr) = sock.accept()
        print(f"Connected {addr}")
        try:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    print("Connection closed")
                    break

                splited = data.split(" ")
                if (len(splited) != 2):
                    print(f"Bad command: {data}")
                    break
                if (splited[0] != "GUESS"):
                    print(f"Bad command: {splited[0]}")
                    break

                val = int(splited[1])
                resp = ""
                if (val > hidden):
                    resp = "LESS"
                elif (val < hidden):
                    resp = "MORE"
                else:
                    resp = "EQUAL"

                conn.send(resp.encode())
                if (resp == "EQUAL"):
                    print("Correct guess, closing")
                    break
        except Exception as e:
            print(f"Exeption: {e}\n")
        finally:
            conn.close()
except KeyboardInterrupt:
    pass
finally:
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    print("Server stoped")