import asyncio
from pprint import pprint
from functools import partial
from trades.trade_parser import TradeParser
from core.constants import POE_ITEM_BASE, POE_CURRENCY_COUNT
from core.async_functions import get_loop_and_executor, run_tasks_then_close_loop
from core.utils import timed_process
from trades.models import Trade


class Crawler:
    trades = []

    def retrieve_and_read_page(self, url):
        parser = TradeParser()
        parser.getTrades(url)
        Trade.objects.bulk_create(parser.trades)


    def crawl_all_pages(self):
        all_poe_items = [POE_ITEM_BASE.format(item_number) for item_number in range(1, POE_CURRENCY_COUNT + 1)]
        loop, executor = get_loop_and_executor(len(all_poe_items))
        tasks = [asyncio.ensure_future(loop.run_in_executor(executor, partial(self.retrieve_and_read_page, poe_page))) for poe_page in all_poe_items]
        run_tasks_then_close_loop(loop, tasks)


    def timed_crawl(self):
        pprint('start!')
        timed_process(self.crawl_all_pages)
