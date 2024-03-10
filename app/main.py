import socket

from app.request import HttpRequest

def handle_connection(conn, addr):
    print("connected to", addr)
    
    http_request = HttpRequest.parse_request(conn.recv(1024))
    method = http_request.method
    
    router = {
        f'{method} /': b"HTTP/1.1 200 OK\r\n\r\n",
    }
    
    
    response = router.get(f'{method} {http_request.url}', b"HTTP/1.1 404 Not Found\r\n\r\n")
    conn.sendall(response)
    conn.close()


def main():
    print("logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.listen(1)
    
    while True:
        print("waiting for a connection...")
        conn, addr = server_socket.accept()
        handle_connection(conn, addr)


if __name__ == "__main__":
    main()
