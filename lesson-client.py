import socket

SOCKET_FILE = "/tmp/faker_socket"

def client():
    client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client_socket.connect(SOCKET_FILE)

    while True:
        message = input("Enter message (or 'exit' to quit): ")
        if message == 'exit':
            break

        client_socket.send(message.encode('utf-8'))

        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received response: {data}")

    client_socket.close()

if __name__ == "__main__":
    client()