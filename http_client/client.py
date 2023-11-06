from aiohttp import ClientSession, ClientResponse
from aiohttp.http_exceptions import HttpProcessingError


class Client:
    base_url: str = 'https://dapp.deals/'
    headers: dict = {}

    def __init__(self):
        self.session = ClientSession(self.base_url, headers=self.headers)

    async def close(self):
        await self.session.close()

    async def get(self, url: str, params: {} = None):
        resp: ClientResponse = await self.session.get(url, params=params)
        return await self.proc(resp)

    async def post(self, url: str, data: {} = None, params: {} = None):
        resp = await self.session.post(url, data=data, params=params)
        return await self.proc(resp)

    @staticmethod
    async def proc(resp: ClientResponse) -> dict | str:
        if not str(resp.status).startswith('2'):
            raise HttpProcessingError(code=resp.status, message=str(resp.content))
        if resp.content_type.endswith('/json'):
            return await resp.json()
        return await resp.text()
