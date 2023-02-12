import unittest
from bs4 import BeautifulSoup
import chardet

from main import Crawler


data_json = '{\
    "keywords": [\
        "añade",\
        "canción",\
        "css"\
    ],\
    "proxies": [\
        "158.69.72.138:9300",\
        "72.170.220.17:8080",\
        "61.220.170.133:8000",\
        "130.41.101.105:8080"\
    ],\
    "type": "Repositories"\
    }'


class TestCrawler(unittest.TestCase):

    def setUp(self):
        self.crawler = Crawler(data_json)
        self.parser = self.crawler.parser()
        self.soup = BeautifulSoup(
            self.crawler.html.text, features='html.parser')

    def test_dataContents(self):
        self.assertTrue(isinstance(self.crawler.data, dict))
        self.assertSetEqual(set(
            self.crawler.data.keys()), set(["keywords", "proxies", "type"]))
        self.assertTrue(isinstance(self.crawler.data["keywords"], list))
        self.assertTrue(isinstance(self.crawler.data["proxies"], list))
        self.assertTrue(isinstance(self.crawler.data["type"], str))
        self.assertGreater(len(self.crawler.data["keywords"]), 0)
        self.assertGreater(len(self.crawler.data["proxies"]), 0)
        self.assertGreater(len(self.crawler.data["type"]), 0)
        self.assertTrue(
            self.crawler.data["type"] in ['Repositories', 'Isuues', 'Wikis'])

        for key in self.crawler.data['keywords']:
            self.assertTrue(isinstance(key, str))
            self.assertTrue(
                chardet.detect(str.encode(key))['encoding'] in ['ascii',
                                                                'utf-8',
                                                                'ISO-8859-9'])

    def test_requests(self):
        self.assertEqual(self.crawler.html.status_code, 200)
        self.assertTrue(isinstance(self.crawler.html.text, str))
        self.assertTrue(isinstance(self.crawler.html.content, bytes))

    def test_beautifulSoup(self):
        self.assertTrue(isinstance(self.soup, BeautifulSoup))
        self.assertIsNotNone(self.soup.find_all(class_='f4 text-normal'))


if __name__ == "__main__":
    unittest.main()
