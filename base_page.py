#создаем класс
class BasePage(object):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

# открываем страницу в браузере
    def open(self):
        self.browser.get(self.url)