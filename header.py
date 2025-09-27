class Header:
    def __init__(self, username=None, password=None, content_type=None, accept=None, cookie=None):
        self.username = username
        self.password = password
        self.content_type = content_type
        self.accept = accept
        self.cookie = cookie

    def create_header(self, header_type="json"):
        if header_type == "json":
            return self._create_json_header(self)
        elif header_type == "token":
            return self._create_token_header(self)
        else:
            raise ValueError(f"Unknown header type: {header_type}")

    def _create_json_header(self, header):
        # private don't access directly
        headers = {
            "username": header.username,
            "password": header.password,
            "content-type": header.content_type,
            "Accept": header.accept,
        }
        return headers

    def _create_token_header(self, header):
        # private don't access directly
        headers = {
            "content-type": header.content_type,
            "Accept": header.accept,
            "cookie": header.cookie,
        }
        return headers
