class HttpRequest:
    def __init__(
        self,
        headers: str = None,
        body: str = None,
        query_params: str = None,
        path_params: str = None,
        url: str = None,
        ipv4: str = None,
    ):
        self.headers = headers
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.ipv4 = ipv4
