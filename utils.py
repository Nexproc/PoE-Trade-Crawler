import datetime
from pprint import pprint


def now():
    return datetime.datetime.now()

def timed_process(fn):
    start = now()
    fn()
    pprint('Total Time For Async: {} seconds'.format((now() - start).seconds))

def do_nothing(*args, **kwargs):
    pass