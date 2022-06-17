"""
Module for Feed class

exports Feed class
"""

import json
import rss_reader_package.utils.config as config
import feedparser
from rss_reader_package.link import Link
from rss_reader_package.utils.exceptions import ConvertJSONError


class Feed:
    """Class which describes normalized Feed object"""
    def __init__(self,
                 source_title: str or None,
                 title: str or None,
                 date: str or None,
                 link: str or None,
                 content: str or None,
                 non_media_links: list[Link] or None,
                 media_links: list[Link] or None
                 ):
        """
        The constructor of Feed class

        Args:
            source_title:       the title of source from where the feed was fetched
            title:              the title of the current feed
            date:               the date of publication of the current feed
            link:               the link where feed is stored
            content:            the content of the current feed
            non_media_links:    non-media links, that are used in the feed
            media_links:        media links, that are used in the feed
        """

        self.source_title = source_title
        self.title = title
        try:
            self.date = date.replace("Z", "+00:00")
        except Exception as e:
            config.verbose_print(f"Feed date is not string ({e})", "warn")
            self.date = date
        self.link = link
        self.content = content
        self.non_media_links = non_media_links
        self.media_links = media_links

    @staticmethod
    def process_feed(feed: feedparser.util.FeedParserDict, source_title: str or None):
        """
        The static function for normalizing fetched feed

        Args:
            feed:           the raw feed object, that was fetched
            source_title:   the source title of fetched news

        Returns:
            Feed: Feed type object, that is already normalized
        """

        feed_source_title = source_title
        config.verbose_print("Scraping feed title", "bold")
        try:
            title = feed.title
        except Exception as e:
            config.verbose_print(f"Warning: Feed title not found ({e})", "warn")
            title = None
        config.verbose_print("Scraping publish date", "bold")
        try:
            date = feed.published
        except Exception as e:
            config.verbose_print(f"Warning: Publish date not found ({e})", "warn")
            date = None
        config.verbose_print("Scraping feed link", "bold")
        try:
            link = feed.link
        except Exception as e:
            config.verbose_print(f"Warning: Feed link not found ({e})", "warn")
            link = None
        config.verbose_print("Scraping feed content", "bold")
        try:
            content = feed.summary
        except Exception as e:
            config.verbose_print(f"Warning: Content not found ({e})", "warn")
            content = None
        config.verbose_print("Scraping non-media links", "bold")
        try:
            non_media_links = list(map(lambda l: Link(l.href, 'link'), feed.links))
        except Exception as e:
            config.verbose_print(f"Warning: Non-media links not found ({e})", "warn")
            non_media_links = []
        config.verbose_print("Scraping media links", "bold")
        try:
            media_links = list(map(lambda l: Link(l['url'], 'image'), feed.media_content))
        except Exception as e:
            config.verbose_print(f"Warning: Media links not found ({e})", "warn")
            media_links = []

        normalized_feed = Feed(
            feed_source_title,
            title,
            date,
            link,
            content,
            non_media_links,
            media_links
        )

        config.verbose_print("Feed object created", "green")

        return normalized_feed

    def to_json(self):
        """
        The function for converting Feed object to JSON string

        Returns:
            JSON string

        Raises:
            ConvertJSONError
        """

        config.verbose_print("Converting feed to JSON format", "blue")
        try:
            return json.dumps(self, default=lambda o: o.__dict__, indent=4)
        except Exception as e:
            raise ConvertJSONError(f"Error when converting feed to JSON ({e})")

    def to_readable(self) -> str:
        """
        The function for converting Feed type object to readable string

        Returns:
            str: Readable string based on Feed object
        """

        config.verbose_print("Converting feed to readable format", "blue")
        all_links = self.non_media_links.copy()
        all_links.extend(self.media_links)
        formatted_links = ""
        for i in range(0, len(all_links)):
            formatted_links += f"[{i + 1}]: {str(all_links[i])}\n"
        if formatted_links == "":
            formatted_links = None

        formatted_feed = \
            f"Feed: {self.source_title}\n\n" + \
            f"Title: {self.title}\n" + \
            f"Date: {self.date}\n" + \
            f"Link: {self.link}\n\n" + \
            f"{self.content}\n\n" + \
            f"Links:\n{formatted_links}\n\n"

        return formatted_feed

    @staticmethod
    def json_to_feed(json_feed: str):
        """
        The function for converting JSON of feed to Feed object

        Args:
            json_feed:  JSON string of feed

        Returns:
            Feed:       Feed object
        """

        converted_feed = json.loads(json_feed)
        non_media_links = list(map(lambda l: Link(l["href"], l["link_type"]), converted_feed["non_media_links"]))
        media_links = list(map(lambda l: Link(l["href"], l["link_type"]), converted_feed["media_links"]))

        return Feed(converted_feed["source_title"],
                    converted_feed["title"],
                    converted_feed["date"],
                    converted_feed["link"],
                    converted_feed["content"],
                    non_media_links,
                    media_links)
