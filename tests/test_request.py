from x_client.aiohttp import Client


async def test_public_request():
    pub = Client()
    resp = await pub._get("https://xync.net")
    assert resp.startswith("<!DOCTYPE html>"), "Bad request"
