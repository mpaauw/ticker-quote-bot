# ticker-quote-bot
A Reddit bot written in Python that displays stock data when summoned and presented with a ticker. **Currently a work-in-progress, yet to be hosted.**

## About
This code implements an accurate, quick, and simple Reddit script that is able to grab relevant financial data upon request. Various functions are supported, such as exception handling, efficient parsing, runtime metrics, and logging. The bot is designed to be easily summoned anywhere on Reddit, while also providing fast data retrieval and guaranteed content delivery.

## Implementation Details
Though it's purpose is simple, during my development process I ran into several issues that allowed me to make careful decisions regarding design and functionality.

### Data Integrity & Efficient Retrieval

- In a scenario where a Reddit user is calling the script in order to quickly request stock data, it would be most appropriate to retrieve the latest quote information available for the ticker in question; I also wanted to rely specifically on an API rather than a scraper. 

   I ended up choosing [Alpha Vantage](https://www.alphavantage.co/) as my data source since they offer a wide array of methods for quickly retrieving cheap, up-to-date financial information on individual firms through their comprehensive API. Other sources I tested were not free to use, did not reflect the latest pricing data, had no publicly-available API, or some combination of these restrictions.

### Listening for Summons / Parsing Reddit

- When I first thought about how to tackle the problem of scanning for summons (or, comments which were requesting a stock quote from the bot), there were many important things to consider. Should comments be flattened within each submission being scanned, or should a breadth-first search algorithm be employed? Should a cache be used for storing summons that were already read or replied to? Which subreddits should be available to the bot?

   Within my first implementation, I chose to test using a simple text file 'cache' that would essentially store the full unique name of any submission comment that was processed, in order to avoid double-tapping any summons within future runs. Essentially, I would scan the top x posts of whichever subreddit the bot was pointing to (in this case, /r/test), flatten all comments within a submission, and search for specific summon keys within each comment, while at the same time checking new comments against existing data within the cache.

   I quickly discovered that this solution was highly inefficient, not only because I was using an archaic form of a cache (if my implementation could even be considered as such), but scanning through dozens of submission threads even within a single subreddit was also quite time consuming and clearly not the best way of determining when and where my bot was being summoned.

- After wrestling with the initial POC design outlined above, I stumbled upon a much more efficient design: reading the bot's mentions via inbox rather than stumbling through an arbitrary number of submissions on any number of subreddits.

   This new methodology requires only a small amount of additional work on the side of the end user (appending '/u/' to their summon call), but would allow the bot to be called from *any* subreddit, only reading comments where it was mentioned (which a huge amount of processing time), and completely skips the need for a cache and instead only parses unread inbox items. This method also allows for the uninhibited parent-child reply tree to exist within any comment thread, preserving the natural ordering of all submission comments without the need for the bot to flatten them within the algorithm.

### Metrics & Analysis

- During testing, I wanted a way to watch the performance of the script unfold in real time, in order to catch bottlenecks and discover various ways of implementing improvements. For this reason, I built a simple metrics engine that collects analytics on number of items parsed and replied, as well as their respective times.

   This data is currently printed to both the console during runtime, as well as preserved within the system's log data.


