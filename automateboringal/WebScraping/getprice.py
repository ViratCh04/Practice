import bs4, requests
# bs4 stands for beautifulsoup4, which parses the html of webpages downloaded by requests module to get a specific text

def getPrice(url):
    req = requests.get(url)
    req.raise_for_status()

    soupObject = bs4.BeautifulSoup(req.text, 'html.parser')         # can make do without html.parser too but an ugly warning will show up(which will not crash the program)
    elements = soupObject.select('#price-including-tax-product-price-12485 > span')             # Looks for the CSS selector to extract the text inside of it
    #category\.product\.list > div.products.wrapper.grid.products-grid > ol > li:nth-child(1) > div > div.product.details.product-item-details > div.product-item-inner > div > div > div.price-box > div > div.prices > div.price-box.price-final_price > span
    price = elements[0].text.strip()
    priceList = open('Hp14sprice.txt', 'wb')
    priceList.write(price.encode())
    priceList.close()
    return price

price = getPrice('https://www.hp.com/in-en/shop/laptops-tablets/hp-laptop-14s-fq1089au-50m59pa.html')
# https://www.hp.com/in-en/shop/laptops-tablets.html
print('Price for your laptop today is ' + price)