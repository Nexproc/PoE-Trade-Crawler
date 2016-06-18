#Poe Trade Ninja
PoE Trade Ninja is made up two main components: the *crawler*, and the *Django + Angular web application*.

## Crawler
Using Python 3.5's asyncio libraries, I'm able to asynchronously crawl poe.trade's currency market. The crawler is able to scrape, parse, and persist all ~5,000 trades in about 3-9 seconds (depending on connection speeds). This script runs once an hour in the background to continue populating data for the trades.

##The Django + Angular Application
Using a series of asynchronous requests, the Angular side of the application is able to gather all of the required aggregated data for each hour in an instant. After fetching all of the trade information for the hour, the client-side application side stores all of the values retrieved (so far) in a cache to prevent any extra, unnecessary calls to the server-side.

## Graphs
I use HighCharts as my graphing library, using a mixture of spline and bar graph types.
