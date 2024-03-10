from app.request import HttpRequest


def status_ok():
    return b"HTTP/1.1 200 OK\r\n\r\n"

def not_found():
    return b"HTTP/1.1 404 Not Found\r\n\r\n"

def echo(request: HttpRequest):
    body = request.path[6:]
    content_type = 'text/plain'
    return f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(body)}\r\n\r\n{body}".encode('utf-8')

def user_agent(request: HttpRequest):
    body = request.headers.get('User-Agent', 'unknown')
    content_type = 'text/plain'
    return f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(body)}\r\n\r\n{body}".encode('utf-8')

def file(request: HttpRequest, directory: str):
    path = request.path.lstrip('/files/')
    if request.method == 'GET':
        try:
            with open(f'{directory}/{path}', 'rb') as f:
                body = str(f.read(), 'utf-8')
                content_type = 'application/octet-stream'
                return f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(body)}\r\n\r\n{body}".encode('utf-8')
        except FileNotFoundError:
            return not_found()
    elif request.method == 'POST':
        with open(f'{directory}/{path}', 'wb') as f:
            f.write(request.body)
            return b'HTTP/1.1 201 OK\r\n\r\n'
    else:
        return b"HTTP/1.1 405 Method Not Allowed\r\n\r\n"
    