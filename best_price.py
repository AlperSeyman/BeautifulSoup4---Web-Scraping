from bs4 import BeautifulSoup
import requests
import re



class Soup():
    def __init__(self,url, search_item):
        self.url = url
        self.search_item = search_item

    def get_content(self):
        r = requests.get(self.url).text
        document = BeautifulSoup(r, "html.parser")
        return document
    
    def create_soup(self):
        soup = self.get_content()
        return soup
    
    def find_page_numbers(self):
        result = self.create_soup()
        page_number = result.find(class_ ="list-tool-pagination-text").strong
        total_page_number = int(str(page_number).split("/")[-2].split(">")[-1][:-1])
        return total_page_number    
    
search_item = input("What product do you want to search ?: ")
#search_item = "3080"
url = f"https://www.newegg.com/p/pl?d={search_item}&N=4131"


soup = Soup(url,search_item)
pages = soup.find_page_numbers()

found_items = {}

for page in range(1, pages + 1):
    url = f"https://www.newegg.com/p/pl?d={soup.search_item}&N=4131&page={page}"
    page = requests.get(soup.url).text
    document = BeautifulSoup(page, "html.parser")
    div = document.find(class_="row-body-border")
    items = div.find_all(string=re.compile(soup.search_item))
    for item in items:
        parent = item.parent
        link = None
        if parent.name != "a":
            continue
        link = parent["href"]
        next_parent = item.find_parent(class_="item-cell")
        price = next_parent.find(class_="price-current")
        if price is not None and price.strong is not None:
            price = price.strong.string
            found_items[item] = {"price":int(price.replace(",","")),"link":link}
        else:
            found_items[item] = {"price":"Price Not Found","link":link}

sorted_items = sorted(found_items.items(), key=lambda x: float(x[1]["price"]) if isinstance(x[1]["price"], (int, float)) else float('inf'))

for item in sorted_items:
   print(item[0])
   print(f"$ {item[1]["price"]}")
   print(f"Link :{item[1]["link"]}")
   print("*******************************************************************")    
