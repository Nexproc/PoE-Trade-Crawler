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
    27: 'Silver Coin',
    28: 'Sacrifice at Dusk',
    29: 'Sacrifice at Midnight',
    30: 'Sacrifice at Dawn',
    31: 'Sacrifice at Noon',
    32: 'Mortal Grief',
    33: 'Mortal Rage',
    34: 'Mortal Hope',
    35: 'Mortal Ignorance',
    36: "Eber's Key",
    37: "Yriel's Key",
    38: "Inya's Key",
    39: "Volkuur's Key",
}

POE_CURRENCY_COUNT = len(CURRENCIES.keys())

VALID_CONTENT_TYPES = {
    'text/html': True,
    'text/html; charset=utf-8': True,
}

DATA_TAG_TO_TRADE_METHOD = {
    'data-sellcurrency': 'set_sell_currency',
    'data-buycurrency': 'set_buy_currency',
    'data-sellvalue': 'set_sell_value',
    'data-buyvalue': 'set_buy_value',
}

NICK = 'http://www.nicktitcombe.com'
GITHUB = 'http://www.github.com'
CURRENT_LEAGUE = "Prophecy"
BASE_SITE_URL = "http://currency.poe.trade/search?league={}".format(CURRENT_LEAGUE)
POE_ITEM_BASE = BASE_SITE_URL + "&online=&want={}&have=1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34"
POE_TRADE_FULL = BASE_SITE_URL + "&online=&want=1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34&have=1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34"
SMALL_POE_TRADE = BASE_SITE_URL + "&online=&want=1-2-3-4-5&have=1-2-3-4-5"
