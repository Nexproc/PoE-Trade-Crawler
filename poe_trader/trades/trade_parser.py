from poe_trader.trades.trade import Trade
from html.parser import HTMLParser
from urllib.request import urlopen
from poe_trader.core.constants import VALID_CONTENT_TYPES, DATA_TAG_TO_TRADE_METHOD
from poe_trader.core.utils import do_nothing

# We are going to create a class called TradeParser that inherits some
# methods from HTMLParser which is why it is passed into the definition
class TradeParser(HTMLParser):
    trades = []

    # This is a function that HTMLParser normally has
    # but we are adding some functionality to it
    def handle_starttag(self, tag, attrs):
        trade = None

        # no need to create a trade object if this tag isn't a trade div
        def get_trade():
            return trade or Trade()

        # We are looking for the begining of a trade. Trades normally look like...
        # <div ... data-sellcurrency="#" data-sellvalue="#" data-buycurrency="#" data-buyvalue="#" ... ></div>
        if tag == 'div':
            for (key, value) in attrs:
                if DATA_TAG_TO_TRADE_METHOD.get(key, None) is not None:
                    trade = get_trade()
                    getattr(trade, DATA_TAG_TO_TRADE_METHOD.get(key), do_nothing)(value)
        if trade:
            trade.set_trade_ratio()
            self.trades.append(trade)

    # This is a new function that we are creating to get trades
    # that our spider() function will call
    def getTrades(self, url):
        self.baseUrl = url
        # Use the urlopen function from the standard Python 3 library
        response = urlopen(url)
        # Make sure that we are looking at HTML and not other things that
        # are floating around on the internet (such as
        # JavaScript files, CSS, or .PDFs for example)
        if VALID_CONTENT_TYPES.get(response.getheader('Content-Type'), False):
            htmlBytes = response.read()
            # Note that feed() handles Strings well, but not bytes
            # (A change from Python 2.x to Python 3.x)
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
