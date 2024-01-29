import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientside, address = s.accept()
    print(f"Connection from {address} has been established")

    # Now, continuously send messages to the client
    while True:
        message = input("Message to send (type 'exit' to close): ")
        
        if message.lower() == 'exit':
            break  # Exit the inner loop if 'exit' is entered

        clientside.send(bytes(message, "utf-8"))

    clientside.close()  # Close the connection when the inner loop exits
