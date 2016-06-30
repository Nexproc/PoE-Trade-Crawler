from collections import OrderedDict

CURRENCIES = OrderedDict({
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
    35: 'Silver Coin',
    36: "Eber's Key",
    37: "Yriel's Key",
    38: "Inya's Key",
    39: "Volkuur's Key",
    40: "Offering to the Goddess",
})

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
ALL_CURRENCY_IDS_STRING = '-'.join([str(key) for key in CURRENCIES.keys()])
BASE_SITE_URL = "http://currency.poe.trade/search?league={}".format(CURRENT_LEAGUE)
POE_ITEM_BASE = BASE_SITE_URL + "&online=x&want={}&have=" + ALL_CURRENCY_IDS_STRING
POE_TRADE_FULL = BASE_SITE_URL + "&online=x&want={0}&have={0}".format(ALL_CURRENCY_IDS_STRING)
SMALL_POE_TRADE = BASE_SITE_URL + "&online=x&want=1-2-3-4-5&have=1-2-3-4-5"
