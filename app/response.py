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
