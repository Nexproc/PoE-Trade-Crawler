CURRENCIES = {
    1: 'Orb of Alteration',
    2: 'Orb of Fusing',
    3: 'Orb of Alchemy',
    4: 'Chaos Orb',
    5: "Gemcutter's Prism",
    6: 'Exalted Orb',
    7: 'Chromatic Orb',
    8: "Jeweller's Orb",
    9: 'Orb of Chance',
    10: "Cartographer's Chisel",
    11: 'Orb of Scouring',
    12: 'Blessed Orb',
    13: 'Orb of Regret',
    14: 'Regal Orb',
    15: 'Divine Orb',
    16: 'Vaal Orb',
    17: 'Scroll of Wisdom',
    18: 'Portal Scroll',
    19: "Armourer's Scrap",
    20: "Blacksmith's Whetstone",
    21: "Glassblower's Bauble",
    22: 'Orb of Transmutation',
    23: 'Orb of Augmentation',
    24: 'Mirror of Kalandra',
    25: 'Eternal Orb',
    26: 'Perandus Coin',
    27: 'Sacrifice at Dusk',
    28: 'Sacrifice at Midnight',
    29: 'Sacrifice at Dawn',
    30: 'Sacrifice at Noon',
    31: 'Mortal Grief',
    32: 'Mortal Rage',
    33: 'Mortal Hope',
    34: 'Mortal Ignorance',
}

POE_CURRENCY_COUNT = len(CURRENCIES.keys())

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

NICK = 'http://www.nicktitcombe.com'
GITHUB = 'http://www.github.com'
POE_ITEM_BASE = "http://currency.poe.trade/search?league=Perandus&online=&want={}&have=1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34"
POE_TRADE_FULL = "http://currency.poe.trade/search?league=Perandus&online=&want=1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34&have=1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34"
SMALL_POE_TRADE = "http://currency.poe.trade/search?league=Perandus&online=&want=1-2-3-4-5&have=1-2-3-4-5"