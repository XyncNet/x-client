from aiohttp import ClientOSError
from aiohttp.http_exceptions import HttpProcessingError

from http_client.client import Client

#decorator for network funcs
def repeat(times: int = 5, wait: int = 3):
    def decorator(func: callable):
        from asyncio import sleep
        async def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return await func(*args, **kwargs)
                except (ClientOSError, HttpProcessingError) as e:
                    print(f'{func.__name__}: attempt {attempt+1}:',  e)
                    await sleep(wait)
            return print('Patience over!')
        return wrapper
    return decorator
