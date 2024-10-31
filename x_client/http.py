from http.client import HTTPSConnection
from json import dumps, loads

from x_client import df_hdrs


class Client:
    host: str
    cn: HTTPSConnection
    headers = df_hdrs

    def __init__(self, host: str = None, headers: dict = None):
        if host:
            self.host = host
        if headers:
            self.headers.update(headers)
        self.cn = HTTPSConnection(self.host, timeout=15)

    def _get(self, url, headers: dict = None) -> dict:
        self.cn.request("GET", url, headers={**self.headers, **(headers or {})})
        return self.__resp()

    def _post(self, url, json: dict = None, headers: dict = None) -> dict:
        headers = headers or {}
        if json:
            json = dumps(json)
            headers.update({"content-type": "application/json;charset=UTF-8"})
        self.cn.request("POST", url, json, {**self.headers, **headers})
        return self.__resp()

    def __resp(self) -> dict:
        resp = self.cn.getresponse().read()
        return loads(resp)

    def close(self):
        self.cn.close()
