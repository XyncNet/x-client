from http_client import Public


async def test_public_request():
    pub = Public('https://ya.ru')
    resp = await pub.get('/')
    assert resp.status == 200, "Bad request"
