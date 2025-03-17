import socket
import faker
import os

SOCKET_FILE = "/tmp/faker_socket"

fake = faker.Faker()

def server():
    if os.path.exists(SOCKET_FILE):
        os.remove(SOCKET_FILE)

    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_socket.bind(SOCKET_FILE)
    server_socket.listen(1)

    print(f"Server listening on {SOCKET_FILE}")

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Received message: {data}")

        # fakerを使用してランダムなメッセージを生成
        response = fake.sentence()
        client_socket.send(response.encode('utf-8'))

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    server()