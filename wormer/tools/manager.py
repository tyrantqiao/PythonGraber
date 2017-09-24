import requests


class UrlsManager:
    def __init__(self):
        self.urls_grabing = []
        self.urls_grabbed = []
        self.rules = ''
        self.response = 0
        self.count = 0

    def has_next_url(self):
        return self.urls_grabing.__len__() != 0

    def get_url(self):
        url = self.urls_grabing.pop()
        self.add_single_url(url, 'urls_grabbed')
        print('start:' + str(self.count) + '=>' + url)
        return url

    def add_urls(self, urls, urls_group='urls_grabing'):
        if urls_group is 'urls_grabing':
            for url in urls:
                if url not in self.urls_grabbed and self.count != 100:
                    self.count += 1
                    print('count:' + str(self.count) + ' =>' + url)
                    self.add_single_url(url)
        else:
            for url in urls:
                if url not in self.urls_grabbed:
                    self.add_single_url(url, 'urls_grabbed')

    def add_single_url(self, url, urls_group='urls_grabing'):
        if urls_group is 'urls_grabing':
            self.urls_grabing.append(url)
        else:
            self.urls_grabbed.append(url)

    def get_nums(self):
        return self.urls_grabing.__len__()


import re


class TextManager:
    def __init__(self):
        self.text = ''

    @staticmethod
    def get_abbreviation(content):
        # TODO make name equal to the text's begin chars
        # return self.text[:3]
        return content[:3]

    @staticmethod
    def find_urls_by_regex(text, url_regex):
        try:
            match_obj = re.findall(url_regex, text)
            return match_obj
        except AttributeError:
            print('no match')
            return None
            # print(text)
            # print(url_regex)
            # print(match_obj)

    @staticmethod
    def find_text_by_regex(page_source, text_pattern):
        print(re.findall(text_pattern, page_source))
        return "".join(re.findall(text_pattern, page_source))


from datetime import datetime


class LogManager:
    def __init__(self):
        self.content = ''
        self.textManager = TextManager()

    def log_text(self, text, text_name=''):
        self.save_text(text_name, text)

    def save_text(self, file_name, text):
        #TODO make the file output to /content/text/
        name = str(self.get_time()) + file_name + '.txt'
        # print(name)
        # print(type(name))
        with open(name, 'w') as file:
            # print("I'm here")
            file.write(text)
            print('save text:' + name)

    def get_time(self):
        return datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    def collect_data(self, page_content):
        self.content += page_content

    def save_all_data(self):
        self.save_text(self.textManager.get_abbreviation(self.content), self.content)
        self.content = ''


# if __name__=='__main__':
#     logger=LogManager()
#     logger.save_text('2015-1-1 122222','hahah')
class ThreadManager(object):
    pass
