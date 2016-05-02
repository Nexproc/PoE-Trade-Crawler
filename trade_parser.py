from trade import Trade
from html.parser import HTMLParser
from urllib.request import urlopen
from constants import VALID_CONTENT_TYPES

# We are going to create a class called TradeParser that inherits some
# methods from HTMLParser which is why it is passed into the definition
class TradeParser(HTMLParser):
    trades = []

    # This is a function that HTMLParser normally has
    # but we are adding some functionality to it
    def handle_starttag(self, tag, attrs):
        trade = None

        def get_trade():
            return trade or Trade()
        # We are looking for the begining of a trade. Trades normally look like...
        # <div ... data-sellcurrency="#" data-sellvalue="#" data-buycurrency="#" data-buyvalue="#" ... ></div>
        if tag == 'div':
            for (key, value) in attrs:
                if key == 'data-sellcurrency':
                    trade = get_trade()
                    trade.set_sell_currency(value)
                if key == 'data-buycurrency':
                    trade = get_trade()
                    trade.set_buy_currency(value)
                if key == 'data-sellvalue':
                    trade = get_trade()
                    trade.set_sell_value(value)
                if key == 'data-buyvalue':
                    trade = get_trade()
                    trade.set_buy_value(value)
        if trade:
            trade.set_trade_ratio()
            self.trades.append(trade)

    # This is a new function that we are creating to get trades
    # that our spider() function will call
    def getTrades(self, url):
        trades = []
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
