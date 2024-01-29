import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    msg = s.recv(1024)

    if not msg:
        print("Server closed the connection.")
        break

    print(msg.decode("utf-8"))
