class HttpRequest:
    def __init__(self, path, method, protocol, headers):
        self.path: str = path
        self.method: str = method
        self.protocol: str = protocol
        self.headers: dict = headers
        
    def __str__(self):
        return f'{self.method} {self.path} {self.protocol}\n{self.headers}'
    
    @staticmethod
    def parse_request(raw_request: bytes) -> 'HttpRequest':
        raw_request = raw_request.decode('utf-8')
        lines = raw_request.split('\r\n')
        method, path, protocol = lines[0].split()
        headers = {}
        
        for line in lines[1:]:
            if line:
                key, value = line.split(': ')
                headers[key] = value

        return HttpRequest(path, method, protocol, headers)
    