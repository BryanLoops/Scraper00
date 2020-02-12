from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

# Opens connection, grabs the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close

# html parsing
page_soup = soup(page_html, 'html.parser')

# print(page_soup.body.span)

# Grabs each product
containers = page_soup.findAll('div', {'class': 'item-container'})

filename = 'products.csv'
f = open(filename, 'w')

headers = "Brand,Product,Price,Shipping\n"

f.write(headers)

for container in containers:
    brand = container.div.find_next('div').a.img['title']
    title_container = container.findAll('a', {'class': 'item-title'})
    product_name = title_container[0].text
    price_container = container.div.find_next('div').find_next('div').find_next('div').ul.li.find_next('li').find_next('li')
    price = "$" + price_container.strong.text + price_container.sup.text
    shipping_container = container.findAll('li', {'class': 'price-ship'})
    shipping = shipping_container[0].text.strip()

    f.write(brand + "," + product_name.replace(",", "|") + "," + price.replace(",", "") + "," + shipping + "\n")


f.close()
