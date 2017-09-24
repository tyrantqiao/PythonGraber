import requests
from wormer.tools import manager
from wormer.data.strategy import GrabStrategy


class DownLoader:
    def __init__(self):
        self.textManager = manager.TextManager()
        self.rules = ''
        self.strategy = ''
        self.url_start = ''

    def get_start(self, url):
        self.url_start = url

    def get_readme(self):
        url = self.url_start + 'robots.txt'
        self.rules = requests.get(url).text
        return self.rules

    # def grabing(self, text, limit, strategy, url_type):
    #     if strategy == GrabStrategy.BREATH_FIRST:
    #         # urls_from_page = self.get_urls_from_page(text, url_type)
    #         return urls_from_page
            # TODO depth-first alogorithms

    @staticmethod
    def grab_single_url(url):
        return requests.get(url)

    def grab_single(self, url_start):
        self.url_start=url_start
