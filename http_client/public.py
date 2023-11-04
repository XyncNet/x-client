from aiohttp import ClientSession, ClientResponse


class Public:
    def __init__(self, base_url: str = None):
        self.session = ClientSession(base_url)

    async def close(self):
        await self.session.close()

    async def get(self, url: str, params: {} = None):
        resp: ClientResponse = await self.session.get(url, params=params)
        return await self.proc(resp)

    async def post(self, url: str, data: {} = None, params: {} = None):
        resp = await self.session.post(url, data=data, params=params)
        return await self.proc(resp)

    @staticmethod
    async def proc(resp: ClientResponse) -> dict | ClientResponse:
        if resp.content_type.endswith('/json'):
            return await resp.json()
        return resp
