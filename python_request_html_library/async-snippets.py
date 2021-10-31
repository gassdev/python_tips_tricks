import time

from requests_html import AsyncHTMLSession
a_session = AsyncHTMLSession()

async def get_delay1():
    r = await a_session.get('https://httpbin.org/delay/1')
    return r

async def get_delay2():
    r = await a_session.get('https://httpbin.org/delay/2')
    return r

async def get_delay3():
    r = await a_session.get('https://httpbin.org/delay/3')
    return r

t1 = time.perf_counter()

results = a_session.run(get_delay1, get_delay2, get_delay3)

for result in results:
    response = result.html.url
    print(response)

t2 = time.perf_counter()

print(f"Asynchronous: {t2 - t1} seconds")
