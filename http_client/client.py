from aiohttp import ClientSession, ClientResponse
from aiohttp.http_exceptions import HttpProcessingError

class HttpNotFound(HttpProcessingError):
    code = 404
    message = 'NotFound'

class Client:
    base_url: str = None
    middle_url: str = ''
    headers: dict = {}

    def __init__(self):
        self.session = ClientSession(self.base_url, headers=self.headers)

    async def close(self):
        await self.session.close()

    async def get(self, url: str, params: {} = None):
        resp: ClientResponse = await self.session.get(self.middle_url+url, params=params)
        return await self.proc(resp)

    async def post(self, url: str, data: {} = None, params: {} = None):
        resp = await self.session.post(self.middle_url+url, json=data, params=params)
        return await self.proc(resp)

    @staticmethod
    async def proc(resp: ClientResponse) -> dict | str:
        if not str(resp.status).startswith('2'):
            if resp.status==404:
                raise HttpNotFound()
            raise HttpProcessingError(code=resp.status, message=str(resp.content))
        if resp.content_type.endswith('/json'):
            return await resp.json()
        return await resp.text()
