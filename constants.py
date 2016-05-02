VALID_CONTENT_TYPES = {
    'text/html': True,
    'text/html; charset=utf-8': True,
}

DATA_TAG_TO_TRADE_METHOD = {
    'data-sellcurrency': 'set_trade_currency',
    'data-buycurrency': 'set_buy_currency',
    'data-sellvalue': 'set_sell_value',
    'data-buyvalue': 'set_buy_value'
}