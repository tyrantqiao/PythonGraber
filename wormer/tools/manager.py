import requests


class UrlsManager:
    def __init__(self):
        self.urls = []
        self.url_grab = ''
        self.rules = ''
        self.response = 0

    def grab(self, url_grab):
        self.url_grab = url_grab
        self.response = requests.get(self.url_grab)
        return self.response

    def get_readme(self):
        url = self.url_grab + 'robots.txt'
        self.rules = self.grab(url).text
        return self.rules


class TextManager:
    def __init__(self):
        self.text = ''

    def get_abbreviation(self):
        # make name equal to the text's begin chars
        # return self.text[:3]
        return 'hah'


from datetime import datetime


class LogManager:
    def __init__(self):
        self.text = ''
        self.textManager = TextManager()

    def log_text(self, text, text_name=''):
        self.save_text(text_name, text)

    def save_text(self, file_name, text):
        name = str(self.get_time()) + file_name + '.txt'
        with open(name, 'w') as file:
            file.write(text)
            print('save text:' + name)

    def get_time(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
