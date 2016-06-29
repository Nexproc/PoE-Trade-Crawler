from trades.models import Trade
from html.parser import HTMLParser
from urllib.request import urlopen, Request, FancyURLopener
from core.constants import VALID_CONTENT_TYPES, DATA_TAG_TO_TRADE_METHOD
from core.utils import do_nothing
from time import sleep
import random


class PoEOpener(FancyURLopener):
    version = "Mozilla/5.0"

class TradeParser(HTMLParser):
    trades = []

    def handle_starttag(self, tag, attrs):
        trade = None

        # no need to create a trade object if this tag isn't a trade div
        def get_trade():
            return trade or Trade()

        # We are looking for the beginning of a trade. Trades normally look like...
        # <div ... data-sellcurrency="#" data-sellvalue="#" data-buycurrency="#" data-buyvalue="#" ... ></div>
        if tag == 'div':
            for (key, value) in attrs:
                if DATA_TAG_TO_TRADE_METHOD.get(key, None) is not None:
                    trade = get_trade()
                    getattr(trade, DATA_TAG_TO_TRADE_METHOD.get(key), do_nothing)(value)
        if trade:
            trade.set_trade_ratio()
            self.trades.append(trade)

    # function to get trades
    def get_trades(self, url):
        # Use the urlopen function from the standard Python 3 library
        # detection defence and prevent my scraper from creating a huge influx on the server
        # use request to feign a Mozilla browser
        opener = PoEOpener()
        # give my web crawler a 10 minute window to randomly scrape
        sleep(random.randrange(600))
        response = opener.open(url)
        # Make sure that we are looking at HTML and not another file type such as .js, .css, .pdf, etc.
        if VALID_CONTENT_TYPES.get(response.getheader('Content-Type'), False):
            htmlBytes = response.read()
            # Note that feed() handles Strings well, but not bytes
            # (A change from Python 2.x to Python 3.x)
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
