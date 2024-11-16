from bs4 import BeautifulSoup
import requests


class Soup():
    def __init__(self,url):
        self.url = url

    def get_content(self):
        r = requests.get(self.url).text
        document = BeautifulSoup(r, "html.parser")
        return document
    
    def create_soup(self):
        soup = self.get_content()
        return soup

    def coin_price(self):
        result = self.create_soup()
        tbody = result.tbody
        trs = tbody.contents

        prices = {}
        for tr in trs[:10]:
            name, price = tr.contents[2:4]
            fixed_name = name.p.string
            fixed_price = price.div.span.string
            prices[fixed_name] = fixed_price

        for key, value in prices.items():
            print(f"{key} : {value}")
                



url = "https://coinmarketcap.com/"


soup = Soup(url)
soup.coin_price()