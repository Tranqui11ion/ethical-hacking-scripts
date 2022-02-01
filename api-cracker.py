# Written for a specific API, however, it would be fairly straight forward
# to modify this for any API that has a sequential id
# API being tested takes input in the form of {SALT}number{HASH}
# Code interates through all combinations of salt and hash 

import requests
import aiohttp
import asyncio

#URL to the API
url = "http://CHANGEME.com"
#Parameter to be tested
id_num = #CHANGE_ID

async def get(session: aiohttp.ClientSession, url: str, **kwargs) -> dict:
    print(f"Requesting status")
    resp = await session.request('GET', url=url, **kwargs)
    print(f'{url} : {resp.status}')
    if resp.status == 200:                      
        stat = await resp.json()
        print(stat['status'])
    return stat

async def main(**kwargs):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for x in range(16028382, 16028388):
                stringx = f'{x:08}'
                hash = f'{stringx[0:3]}{id_num}{stringx[3:]}'
                url = f'url{hash}'
                tasks.append(get(session=session, url=url, **kwargs))
        htmls = await asyncio.gather(*tasks, return_exceptions=True)
        return htmls


if __name__ == '__main__':
    asyncio.run(main())  # Python 3.7+





        
