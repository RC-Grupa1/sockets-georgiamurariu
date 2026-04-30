import socket

HOST = "100.111.244.31"
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Client: ")
    client.sendto(message.encode("utf-8"), (HOST, PORT))

    if message.lower() == "exit":
        break

    response, server_address = client.recvfrom(1024)
    print("Server:", response.decode("utf-8"))

client.close()