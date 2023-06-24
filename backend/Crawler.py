import logging
import requests
from bs4 import BeautifulSoup
logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)
# logging.info('This is an info message')
# logging.warning('This is a warning message')
class Crawler:

    def __init__(self, urls=[]):
        self.visited_urls = []
        self.urls_to_visit = urls

    def download_url(self, url):
        session = requests.Session()
        # session.get(url)
        response = session.get(url)
        soup = BeautifulSoup(response.content, 'html.parser').get_text()
        return soup

    # def add_url_to_visit(self, url):
    #     if url not in self.visited_urls and url not in self.urls_to_visit:
    #         self.urls_to_visit.append(url)

    def crawl(self, url):
        symbols = "!\"#\'%&()*+-./;<=>?@[]^_`{|}~½¼²¾½=<>↉⅓⅔¼¾⅕?⅖⅗⅘⅙⅚⅐\⅛⅜⅝⅞⅑⅒"
        real_content = []
        sitecontent = self.download_url(url)
        documents = sitecontent.splitlines()
        for line in documents:
            if line not in ("SYM", "'", "-", "''", "``", "LS", ".", "!", "?", ",", ":", "(", ")", "\"", "#", "$", "...", "--",";", "{","}", "`", "½", "¼", '²', '2²', "", 'id_right', 'text_right', '', '«', '»'):
                real_content.append(line)
        document = ""
        for line in real_content:
            document = document.__add__(line+"\n")
        # document2 = document[0]
        for i in range(len(symbols)):
            document = document.replace(symbols[i], '')
        return document

    def run(self):
        all_result = []
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                all_result.append(self.crawl(url))
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited_urls.append(url)
        print(all_result)
        return all_result

# if __name__ == '__main__':
#     Crawler(urls=['http://www.bookofjoe.com/2005/11/worlds_most_exp.html','http://en.wikipedia.org/wiki/Main_Page']).run()