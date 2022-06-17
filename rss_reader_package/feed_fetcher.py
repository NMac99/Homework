"""
Module for FeedFetcher class

exports FeedFetcher class
"""
import feedparser
import rss_reader_package.utils.config as config
from datetime import datetime
from rss_reader_package.feed import Feed
from rss_reader_package.cache_worker import CacheWorker
from rss_reader_package.utils.exceptions import WrongLimitError, WrongUrlError


class FeedFetcher:
    """Class for fetching feeds and storing feeds using feedparser.py"""

    def __init__(self, source: str, limit: int or None):
        """
        The constructor for FeedFetcher class

        Args:
            source: the source url of rss feeds
            limit:  limit of the feeds, that must be shown

        Raises:
            WrongLimitError
        """

        if limit is not None and limit < 1:
            raise WrongLimitError("Argument LIMIT must be greater than 0")

        self.__source = source
        self.__limit = limit
        self.feeds = []
        self.feeds_formatted = []

    def fetch_feeds(self):
        """The function that fetches and stores feeds using source and limit of object """

        self.feeds = feedparser.parse(self.__source)
        if "entries" not in self.feeds or len(self.feeds.entries) < 1:
            raise WrongUrlError("Specified url is not rss type")
        config.verbose_print("Feeds fetched", "green")
        if self.__limit is None:
            limit = len(self.feeds.entries)
        else:
            limit = min(len(self.feeds.entries), self.__limit)
        for i in range(0, limit):
            self.feeds_formatted.append(
                Feed.process_feed(self.feeds.entries[i], self.feeds.feed.title)
            )
        config.verbose_print("Storing fetched feeds in cache", "bold")
        for f in self.feeds_formatted:
            CacheWorker.store_feed_in_cache(str(datetime.fromisoformat(f.date).date()),
                                            self.__source,
                                            f.to_json(),
                                            f.link)
