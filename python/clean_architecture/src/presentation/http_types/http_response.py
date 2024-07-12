class HttpResponse:
    def __init__(self, status_code: str = None, body: dict = None):
        self.status_code = status_code
        self.body = body
