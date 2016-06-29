import asyncio
from pprint import pprint
from functools import partial
from trades.trade_parser import TradeParser
from core.constants import POE_ITEM_BASE, POE_CURRENCY_COUNT
from core.async_functions import get_loop_and_executor, run_tasks_then_close_loop
from core.utils import timed_process
from trades.models import Trade, HourlyTradeAggregate


class Crawler:
    def retrieve_and_read_page(self, url):
        parser = TradeParser()
        parser.get_trades(url)
        return parser.trades

    def process_trade_data(self):
        HourlyTradeAggregate.create_trade_aggregations_for_this_hour()

    @timed_process
    def crawl_all_pages(self):
        all_poe_items = [POE_ITEM_BASE.format(item_number) for item_number in range(1, POE_CURRENCY_COUNT + 1)]
        loop, executor = get_loop_and_executor(len(all_poe_items))
        tasks = [asyncio.ensure_future(loop.run_in_executor(executor, partial(self.retrieve_and_read_page, poe_page))) for poe_page in all_poe_items]
        all_trades = []
        for trades in loop.run_until_complete(asyncio.gather(*tasks)):
            all_trades += trades
        loop.close()
        Trade.objects.bulk_create(all_trades)
        # whatever processing needs to happen with trades should happen here
        self.process_trade_data()
        # clear all trades after they've been processed
        Trade.objects.all().delete()
