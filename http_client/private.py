from aiohttp import ClientSession

from http_client.public import Public


class Private(Public):
    headers: dict

    # noinspection PyMissingConstructor
    def __init__(self, base_url: str = None, headers: dict = None):
        self.headers = headers
        self.session = ClientSession(base_url, headers=headers)
