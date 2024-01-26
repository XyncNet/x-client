from http_client.client import Client

#decorator for network funcs
def repeat_on_fault(times: int = 4, wait: int = 3):
    def decorator(func: callable):
        from asyncio import sleep
        async def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    print(f'{func.__name__}: attempt {attempt+1}:',  e)
                    await sleep(wait)
            return print('Patience over!')
        return wrapper
    return decorator
