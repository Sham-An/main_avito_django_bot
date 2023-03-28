import asyncio
import httpx
import time
from typing import Callable, List
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
#cd avito_parser_django\avito
#I:\pythonProjects\avito_django_telebot\avito_parser_django\avito> python manage.py httpx_class1


#from rich import print


class DadJokes:

    headers = dict(Accept='application/json')

    def __init__(self):
        """
        Since we want to reuse the client, we can't use a context manager that closes it.
        We need to use a loop to exert more control over when the client is closed.
        """
        self.client = httpx.AsyncClient(headers=self.headers)
        self.loop = asyncio.get_event_loop()

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
        # start = time.time()
        group = asyncio.gather(*(self._get(url, idx=idx) for idx, url in enumerate(urls)))
        # self.loop.run_until_complete(group)
        # print("Runtime: ", int((time.time() - start) * 1000))
        print(f"group {group}")


    def get_one(self, urls: List[str]):
        # start = time.time()
        group = asyncio.gather(*(self._get(url, idx=idx) for idx, url in enumerate(urls)))
        # self.loop.run_until_complete(group)
        # print("Runtime: ", int((time.time() - start) * 1000))
        print(f"group {group}")


# url = 'https://www.icanhazdadjoke.com'
# dj = DadJokes()
# dj.get_many([url for x in range(4)])


class Command(BaseCommand):
    help = 'Парсинг Avito'

    def handle(self, *args, **options):
        # p = AvitoParser()
        # p.parse_all()
        url = 'https://www.icanhazdadjoke.com'
        url = 'https://www.avito.ru/rostovskaya_oblast_aksay/mototsikly_i_mototehnika/mopedy_i_skutery-ASgBAgICAUQ82gE?cd=1&q=%D1%81%D0%BA%D1%83%D1%82%D0%B5%D1%80&radius=200&searchRadius=200'
        dj = DadJokes()
        dj.get_one([url for x in range(4)])
