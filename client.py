import asyncio
from enum import Enum
import json

import requests
from obj import SignalData, SmartWallet, StoryData


base_url = 'https://debot.ai/api'


class Chain(Enum):
    SOL = 'solana'
    ETH = 'eth'
    

class SmartWalletSortField(Enum):
    PNL_1D = 'pnl_1d'
    PNL_7D = 'pnl_7d'
    PNL_30D = 'pnl_30d'


class DebotClient:
    def __init__(self, headers_json_path:str):
        with open(headers_json_path, 'r') as f:
            self._headers = json.load(f)
            
    async def get(self, url:str) -> dict:
        resp = await asyncio.to_thread(requests.get, url, headers=self._headers)
        if resp.status_code != 200:
            raise Exception(f'Failed to get: {resp.status_code}')
        res = resp.json()
        if res['code'] != 0:
            raise Exception(f'Failed to get: {res["message"]}')
        return res['data']

    async def signals(self, *, tokens:list[str]=None, page_size:int=24, start_time:int=None, next_page:int=None) -> SignalData:
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
        return await self.get(url)

    async def story(self, token:str) -> StoryData:
        url = f'{base_url}/story/?token={token}'
        return await self.get(url)

    async def smart_wallets(self, *, chain:Chain, sort_field: SmartWalletSortField=None, sort_order: str='desc', is_new_recommend: bool=False) -> SmartWallet:
        url = f'{base_url}/dashboard/wallet/smart_wallet?'
        query = f'chain={chain.value}'
        if sort_field:
            query += f'&sort_field={sort_field.value}'
        if sort_order:
            query += f'&sort_order={sort_order}'
        if is_new_recommend:
            query += f'&is_new_recommend={str(is_new_recommend).lower()}'
        return await self.get(url + query)


if __name__ == '__main__':
    client = DebotClient('header_test.json')
    # res = asyncio.run(client.signals())
    # res = asyncio.run(client.story('B3cif6B4FxUWK75VbUzG7ymxAxkozXEC4XLA6fFVpump'))
    res = asyncio.run(client.smart_wallets(chain=Chain.SOL, sort_field=SmartWalletSortField.PNL_7D, is_new_recommend=True))
    print(res)
