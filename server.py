import socket

HOST = '127.0.0.1'
PORT = 8080

# Valid credentials
USERNAME = "admin"
PASSWORD = "1234"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server waiting for connection...")
conn, addr = server.accept()
print("Connected by", addr)

username = conn.recv(1024).decode()
password = conn.recv(1024).decode()

if username == USERNAME and password == PASSWORD:
    conn.send("AUTH_SUCCESS".encode())
    print("Client authenticated")

    while True:
        msg = conn.recv(1024).decode()
        if msg.lower() == "exit":
            break
        print("Client:", msg)

        reply = input("Server: ")
        conn.send(reply.encode())
else:
    conn.send("AUTH_FAILED".encode())
    print("Authentication failed")

conn.close()
server.close()
