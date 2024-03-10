import socket

def handle_connection(conn, addr):
    print("Connected to", addr)
    conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.close()


def main():
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.listen(1)
    
    while True:
        print("Waiting for a connection...")
        conn, addr = server_socket.accept()
        handle_connection(conn, addr)


if __name__ == "__main__":
    main()
