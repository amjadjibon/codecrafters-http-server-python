import socket

from app.request import HttpRequest
from app.response import status_ok, not_found, echo, user_agent

def handle_connection(conn, addr):
    print("connected to", addr)
    
    http_request = HttpRequest.parse_request(conn.recv(1024))
    
    if http_request.path == '/':
        response = status_ok()
    elif http_request.path.startswith('/echo/'):
        response = echo(http_request)
    elif http_request.path == '/user-agent':
        response = user_agent(http_request)
    else:
        response = not_found()
    
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
