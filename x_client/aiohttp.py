from aiohttp import ClientSession, ClientResponse
from aiohttp.http_exceptions import HttpProcessingError

from x_client import HttpNotFound, df_hdrs


class Client:
    headers: dict[str, str] = df_hdrs

    def __init__(self, host: str = None, headers: dict[str, str] = None, cookies: dict[str, str] = None):
        if headers:
            self.headers.update(headers)
        self.session = ClientSession("https://" + host if host else None, headers=self.headers, cookies=cookies)

    async def close(self):
        await self.session.close()

    async def _get(self, url: str, params: {} = None):
        resp: ClientResponse = await self.session.get(url, params=params)
        return await self._proc(resp)

    async def _post(self, url: str, data: {} = None, params: {} = None):
        dt = {"json" if isinstance(data, dict) else "data": data}
        resp = await self.session.post(url, **dt, params=params)
        return await self._proc(resp, data)

    async def _delete(self, url: str, params: {} = None):
        resp: ClientResponse = await self.session.delete(url, params=params)
        return await self._proc(resp)

    @staticmethod
    async def _proc(resp: ClientResponse, data=None) -> dict | str:
        if not str(resp.status).startswith("2"):
            if resp.status == 404:
                raise HttpNotFound()
            raise HttpProcessingError(code=resp.status, message=await resp.text())
        if resp.content_type.endswith("/json"):
            return await resp.json()
        return await resp.text()
