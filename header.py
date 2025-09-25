class Header:
    def __init__(self, authorization, content_type, accept, lang, permissions):
        self.authorization = authorization
        self.content_type = content_type
        self.accept = accept
        self.permissions = permissions

    def create_header(self, header_type="json"):
        if header_type == "json":
            return self._create_json_header(self)
        elif header_type == "text":
            return self._create_text_header(self)
        else:
            raise ValueError(f"Unknown header type: {header_type}")

    def _create_json_header(self, header):
        # private don't access directly
        headers = {
            "authorization": header.authorization,
            "content-type": header.content_type,
            "Accept": header.accept,
            "Accept-Language": header.accept_lang,
        }
        return headers

    def _create_text_header(self, header):
        # private don't access directly
        headers = {
            "authorization": header.authorization,
            "content-type": header.content_type,
            "Accept": header.accept,
            "Accept-Language": header.accept_lang,
        }
        return headers
