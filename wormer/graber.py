from wormer.tools import manager, downloader
from wormer.data import strategy
import re


class Graber:
    synopsis_pattern = '''(?=lemma-summary")(.*?)(?<=config) '''
    text_pattern = '>\s*?([^\&\b\n\[\]]*?)<'
    href_pattern = '<a target=_blank href="(/item/[\w\d%]*?)">'

    def __init__(self):
        self.urlManager = manager.UrlsManager()
        self.downloader = downloader.DownLoader()
        self.textManager = manager.TextManager()
        self.logManager = manager.LogManager()
        self.threadManager = manager.ThreadManager()
        self.url_start = ''

    def get_readme(self):
        self.downloader.grab_single(self.url_start)
        tips = self.downloader.get_readme()
        return tips

    def grabing_urls(self, limit=100, grab_strategy=strategy.GrabStrategy.BREATH_FIRST):
        self.urlManager.add_single_url(self.url_start)
        self.urlManager.add_single_url(self.url_start, 'urls_grabbed')
        while self.urlManager.has_next_url():
            page_source = self.downloader.grab_single_url(self.urlManager.get_url()).content.decode('utf-8')

            # match need to the beginning of the string, and return is a turple, use [i for i in turple] to change, and findall return list
            urls = self.textManager.find_urls_by_regex(page_source, Graber.href_pattern)
            synopsis = self.textManager.find_text_by_regex(page_source, Graber.synopsis_pattern, re.VERBOSE|re.MULTILINE|re.DOTALL)
            # print(synopsis)
            page_content = self.textManager.find_text_by_regex(synopsis, Graber.text_pattern, re.VERBOSE|re.MULTILINE|re.DOTALL)
            if urls and page_content is not None:
                self.add_urls_head(urls, 'https://baike.baidu.com')
                self.urlManager.add_urls(urls)
                self.logManager.collect_data(page_content)
        self.logManager.save_all_data()

    @staticmethod
    def add_urls_head(urls, head):
        for i, item in enumerate(urls):
            item = head + item
            urls[i] = item

    def get_start(self, url_start):
        self.url_start = url_start


if __name__ == '__main__':
    # url = input('The website you want:\n')
    url_python_baike = 'https://baike.baidu.com/item/Python'
    graber = Graber()
    graber.get_start(url_python_baike)
    graber.grabing_urls()

    # text = graber.get_readme(url)

    # graber.logManager.log_text(text)
