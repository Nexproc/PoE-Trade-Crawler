from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
from pprint import pprint
import asyncio
import datetime
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from websites import POE_ITEM_BASE
from misc_constants import POE_CURRENCY_COUNT

now = datetime.datetime.now

# We are going to create a class called LinkParser that inherits some
# methods from HTMLParser which is why it is passed into the definition
class LinkParser(HTMLParser):


    # This is a function that HTMLParser normally has
    # but we are adding some functionality to it
    def handle_starttag(self, tag, attrs):
        # We are looking for the begining of a link. Links normally look
        # like <a href="www.someurl.com"></a>
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    # We are grabbing the new URL. We are also adding the
                    # base URL to it. For example:
                    # www.netinstructions.com is the base and
                    # somepage.html is the new URL (a relative URL)
                    #
                    # We combine a relative URL with the base URL to create
                    # an absolute URL like:
                    # www.netinstructions.com/somepage.html
                    newUrl = parse.urljoin(self.baseUrl, value)
                    # And add it to our colection of links:
                    self.links = self.links + [newUrl]

    # This is a new function that we are creating to get links
    # that our spider() function will call
    def getLinks(self, url):
        self.links = []
        # Remember the base URL which will be important when creating
        # absolute URLs
        self.baseUrl = url
        # Use the urlopen function from the standard Python 3 library
        response = urlopen(url)
        pprint(response)
        # Make sure that we are looking at HTML and not other things that
        # are floating around on the internet (such as
        # JavaScript files, CSS, or .PDFs for example)
        valid_content_types = {
            'text/html': True,
            'text/html; charset=utf-8': True,
        }
        if valid_content_types.get(response.getheader('Content-Type'), False):
            htmlBytes = response.read()
            # Note that feed() handles Strings well, but not bytes
            # (A change from Python 2.x to Python 3.x)
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString, self.links
        else:
            pprint("Invalid header")
            return "", []

# And finally here is our spider. It takes in an URL, a word to find,
# and the number of pages to search through before giving up
def spider(url, word, maxPages):
    start = now()
    pagesToVisit = [url]
    numberVisited = 0
    foundWord = False
    # The main loop. Create a LinkParser and get all the links on the page.
    # Also search the page for the word or string
    # In our getLinks function we return the web page
    # (this is useful for searching for the word)
    # and we return a set of links from that web page
    # (this is useful for where to go next)
    while numberVisited < maxPages and pagesToVisit != [] and not foundWord:
        numberVisited = numberVisited + 1
        # Start from the beginning of our collection of pages to visit:
        url = pagesToVisit[0]
        pagesToVisit = pagesToVisit[1:]
        pprint("{} Visiting: {}".format(numberVisited, url))
        parser = LinkParser()
        data, links = parser.getLinks(url)
        if data.find(word)>-1:
            foundWord = True
            # Add the pages that we visited to the end of our collection
            # of pages to visit:
            pagesToVisit = pagesToVisit + links
            pprint("**Success!**")
    if foundWord:
        pprint("The word {} was found at {}.".format(word, url))
    else:
        pprint("Word never found")

    total_time = now() - start
    pprint("Finished in: {} seconds".format(total_time.seconds))

def get_loop_and_executor(executor_size):
    loop = asyncio.get_event_loop()
    executor = ProcessPoolExecutor(executor_size)
    return loop, executor

def run_tasks_then_close_loop(loop, tasks):
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

def crawl_all_pages():
    all_poe_items = [POE_ITEM_BASE.format(item_number) for item_number in range(1, POE_CURRENCY_COUNT)]
    loop, executor = get_loop_and_executor(len(all_poe_items))
    tasks = [asyncio.ensure_future(loop.run_in_executor(executor, partial(spider, poe_page, 'Chaos Orb', 1))) for poe_page in all_poe_items]
    run_tasks_then_close_loop(loop, tasks)

def timed_process(fn):
    start = now()
    fn()
    pprint('Total Time For Async: {} seconds'.format((now() - start).seconds))

def timed_crawl():
    timed_process(crawl_all_pages)

timed_crawl()