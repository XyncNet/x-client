from http_client import Client


async def test_public_request():
    pub = Client()
    resp = await pub.get('/')
    assert resp.startswith('<!DOCTYPE html>'), "Bad request"
