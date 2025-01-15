import asyncio

import requests
from obj import SignalData, StoryData


base_url = 'https://debot.ai/api'

async def signals(*, tokens:list[str]=None, page_size:int=24, start_time:int=None, next_page:int=None) -> SignalData:
    url = f'{base_url}/official/signal/channel/list?'
    query = ''
    if start_time:
        query += f'&start_time={start_time}'
    if next_page:
        query += f'&next={next_page}'
    if page_size:
        query += f'&page_size={page_size}'
    if tokens:
        for token in tokens:
            query += f'&tokens={token}'
    if query:
        url += f'{query.strip("&")}'
    resp = await asyncio.to_thread(requests.get, url)
    if resp.status_code != 200:
        raise Exception(f'Failed to get signals: {resp.status_code}')
    res = resp.json()
    if res['code'] != 0:
        raise Exception(f'Failed to get signals: {res["message"]}')
    return res['data']


async def story(token:str) -> StoryData:
    url = f'{base_url}/story/?token={token}'
    resp = await asyncio.to_thread(requests.get, url)
    if resp.status_code != 200:
        raise Exception(f'Failed to get story: {resp.status_code}')
    res = resp.json()
    print(res)
    if res['code'] != 0:
        raise Exception(f'Failed to get story: {res["message"]}')
    return res['data']


if __name__ == '__main__':
    res = asyncio.run(story("B3cif6B4FxUWK75VbUzG7ymxAxkozXEC4XLA6fFVpump"))
    print(res)
