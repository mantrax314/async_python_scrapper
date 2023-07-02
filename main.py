import asyncio
import os
import re
from datetime import datetime
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup


async def scrap_price(product):
    payload = {'api_key': os.getenv('SCRAPEOPS_API_KEY'), 'url': product.url, 'country': 'us'}
    url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.find('span', {'class': product.scrap_field})
        if price_element:
            price_text = price_element.text
            pattern = r"\$[\d.]+"
            match = re.search(pattern, price_text)
            if match:
                product.price = float(match.group(0).replace('$', ''))
                return product
            return None
    else:
        print("Error status code ", response.status_code)
    return None


async def main(products):
    print("started at {}".format(datetime.now()))

    def_await = []
    products_res = []
    for product in products:
        def_await.append(asyncio.create_task(scrap_price(product)))

    for i, await_ in enumerate(def_await):
        aw = await await_
        products_res.append(aw)
    print("finished at {}".format(datetime.now()))
    return products_res

