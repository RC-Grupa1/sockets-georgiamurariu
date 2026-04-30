import socket

HOST = "100.111.244.31"
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    message = input("Client: ")
    client.send(message.encode("utf-8"))

    if message.lower() == "exit":
        break

    response = client.recv(1024).decode("utf-8")
    print("Server:", response)

client.close()