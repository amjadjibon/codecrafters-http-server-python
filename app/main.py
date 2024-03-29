import socket
import sys
import threading

from app.request import HttpRequest
from app.response import file, status_ok, not_found, echo, user_agent

def handle_connection(conn, addr, directory):
    print("connected to", addr)
    
    http_request = HttpRequest.parse_request(conn.recv(1024))
    
    if http_request.path == '/':
        response = status_ok()
    elif http_request.path.startswith('/echo/'):
        response = echo(http_request)
    elif http_request.path == '/user-agent':
        response = user_agent(http_request)
    elif http_request.path.startswith('/files/'):
        response = file(http_request, directory)
    else:
        response = not_found()
    
    conn.sendall(response)
    conn.close()

def get_directory():
    args = sys.argv
    
    if "--directory" in args:
        index = args.index("--directory")
        return args[index + 1]
    
    return "."        
    

def main():
    print("logs from your program will appear here!")
    
    directory = get_directory()
    print(f"using directory: {directory}")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.listen(1)
    
    while True:
        print("waiting for a connection...")
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_connection, args=(conn, addr, directory))
        thread.start()


if __name__ == "__main__":
    main()
