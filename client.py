import socket

HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Username: ")
password = input("Password: ")

client.send(username.encode())
client.send(password.encode())

response = client.recv(1024).decode()

if response == "AUTH_SUCCESS":
    print("Authentication successful")

    while True:
        msg = input("Client: ")
        client.send(msg.encode())
        if msg.lower() == "exit":
            break

        reply = client.recv(1024).decode()
        print("Server:", reply)
else:
    print("Authentication failed. Connection closed.")

client.close()
