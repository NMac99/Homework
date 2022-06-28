import unittest
from rss_reader_package.mocks.raw_feed_mock import mock_feed_raw
from rss_reader_package.feed import Feed


class TestFeed(unittest.TestCase):
    parsed_feed = Feed.json_to_feed(mock_feed_raw)

    def test_process_feed(self):
        self.assertIsNone(TestFeed.parsed_feed.source_title)
        self.assertEqual(TestFeed.parsed_feed.title, "Taiwanese F-16 fighter makes emergency landing in Hawaii")
        self.assertEqual(TestFeed.parsed_feed.date, "2022-06-07T19:16:43Z")
        self.assertEqual(TestFeed.parsed_feed.link,
                         "https://news.yahoo.com/taiwanese-f-16-fighter-makes-191643064.html")
        self.assertIsNone(TestFeed.parsed_feed.content)
        self.assertEqual(len(TestFeed.parsed_feed.non_media_links), 0)
        self.assertEqual(TestFeed.parsed_feed.media_links[0].href,
                         "https://s.yimg.com/uu/api/res/1.2/xEduvF_K_md_I0S4N_bKPA--~B/"
                         "aD0zMzMzO3c9NTAwMDthcHBpZD15dGFjaHlvbg--/"
                         "https://media.zenfs.com/en/ap.org/d6b6186493eecb5a8085e62472973496")

    def test_to_json(self):
        self.assertEqual(type(TestFeed.parsed_feed.to_json()), str)
        self.assertEqual(len(TestFeed.parsed_feed.to_json()), 540)

    def test_to_readable(self):
        self.assertEqual(type(TestFeed.parsed_feed.to_json()), str)
        self.assertEqual(len(TestFeed.parsed_feed.to_json()), 374)


unittest.main()
