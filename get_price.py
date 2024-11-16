from bs4 import BeautifulSoup
import requests


class Soup():
    def __init__(self, url):
        self.url = url

    def get_content(self):
        r = requests.get(self.url)
        content = r.text
        documnet = BeautifulSoup(content, "html.parser")
        return documnet
    
    def create_soup(self):
        soup = self.get_content()
        return soup
    
    def find_price(self):
        result = self.create_soup()
        price = result.find_all(string="$")
        parent_tag = price[0].parent
        strong_tag = parent_tag.find("strong").string
        return strong_tag



url = "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-10gd/p/N82E16814932459"

soup = Soup(url)
price=soup.find_price()
print(f"$ {price}")