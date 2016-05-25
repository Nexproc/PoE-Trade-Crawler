import datetime
from pprint import pprint


def now():
    return datetime.datetime.now()

def timed_process(fn):
    def decorator(*args):
        start = now()
        result = fn(*args)
        pprint('Total Runtime: {} seconds'.format((now() - start).seconds))
        return result
    return decorator

def do_nothing(*args, **kwargs):
    pass
