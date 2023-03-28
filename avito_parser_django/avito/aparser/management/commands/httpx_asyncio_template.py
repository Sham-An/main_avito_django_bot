import asyncio
import httpx
import time
from typing import Callable, List
#pip install Rich
#pip install discord.py[voice]
from rich import print


class DadJokes:

    headers = dict(Accept='application/json')

    def __init__(self):
        """
        Since we want to reuse the client, we can't use a context manager that closes it.
        We need to use a loop to exert more control over when the client is closed.
        """
        self.client = httpx.AsyncClient(headers=self.headers)
        self.loop = asyncio.new_event_loop()
        #self.loop = asyncio.get_event_loop()

    async def close(self):
        # httpx.AsyncClient.aclose must be awaited!
        await self.client.aclose()

    def __del__(self):
        """
        A destructor is provided to ensure that the client and the event loop are closed at exit.
        """
        # Use the loop to call async close, then stop/close loop.
        self.loop.run_until_complete(self.close())
        self.loop.close()

    async def _get(self, url: str, idx: int = None):
        start = time.time()
        response = await self.client.get(url)
        print(response.json(), int((time.time() - start) * 1000), idx)

    def get(self, url: str):
        self.loop.run_until_complete(self._get(url))

    def get_many(self, urls: List[str]):
        start = time.time()
        group = asyncio.gather(*(self._get(url, idx=idx) for idx, url in enumerate(urls)))
        #group = await asyncio.gather(*(self._get(url, idx=idx) for idx, url in enumerate(urls)))
        self.loop.run_until_complete(group)
        print("Runtime: ", int((time.time() - start) * 1000))


url = 'https://www.icanhazdadjoke.com'
dj = DadJokes()
print(dj)
dj.get_many([url for x in range(4)])
