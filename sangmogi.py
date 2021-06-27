from bs4 import BeautifulSoup as bs
import requests

class Refresher:
    def init(self, url):
        self.url = url
        self.stockno = []
        self.in_stock = False

    def get(self, printout=False):
        req = requests.get(self.url)
        html = bs(req.content, 'lxml')
        no_sale = html.find("p", {'class': 'sideBtn is-primary is-disabled'})
        if no_sale is not None:
            if printout is True:
                print(no_sale.text)
            else:
                pass
        else:
            for element in html.find_all("div", {"class": "slt_box open"}):
                for stat in element.find_all("a", {"data-arg": "1"}):
                    print(str(stat['data-stockno']))
                    self.stockno.append(str(stat['data-stockno']))
            if printout is True:
                print(self.stockno)

    def loop(self, printout=False):
        while not self.stockno:
            self.get(printout=printout)

    def get_known(self):
        if self.in_stock is False:
            req = requests.get(self.url)
            html = bs(req.content, 'lxml')
            no_sale = html.find("p", {'class': 'no_sale'})
            if no_sale is not None:
                print(no_sale.text)
            else:
                self.in_stock = True

    def loop_known(self):
        while self.in_stock is False:
            self.get_known()

if __name__ == '__main__':
    R = Refresher('https://tickets.interpark.com/goods/21005562')
    R.get(printout=True)