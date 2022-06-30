import requests as req
import json


def date_format(date_input):
    if "century" in date_input:
        if "-" in date_input:
            index = date_input.find("th")
            if index > 2:
                date_input = date_input[index - 2:index] + "00"
            else:
                date_input = date_input[index - 1:index] + "00"
        else:
            date_input = date_input[:2] + "00"
    elif "-" in date_input and "century" not in date_input:
        date_input = date_input[:4]
    return date_input


def get_item_price(url_input):
    item_number = url_input.split("item")[1].strip(' ').split('/')[1]
    url = f"http://pstrial-2022-05-20.toscrape.com/api/price/{item_number}"
    response = req.get(url)
    price_dict = json.loads(response.text)
    return "$" + price_dict['price']
