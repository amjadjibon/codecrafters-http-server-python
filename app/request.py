class HttpRequest:
    def __init__(self, path, method, protocol, headers, body):
        self.path: str = path
        self.method: str = method
        self.protocol: str = protocol
        self.headers: dict = headers
        self.body: bytes = body
        
    def __str__(self):
        return f'{self.method} {self.path} {self.protocol}\n{self.headers}'
    
    @staticmethod
    def parse_request(raw_request: bytes) -> 'HttpRequest':
        raw_request = raw_request.decode('utf-8')
        lines = raw_request.split('\r\n')
        method, path, protocol = lines[0].split()
        headers = {}
        body = b''
        
        for i in range(1, len(lines)):
            if lines[i]:
                key, value = lines[i].split(': ')
                headers[key] = value
            else:
                body = lines[i+1]
                break

        return HttpRequest(path, method, protocol, headers, body.encode('utf-8'))
