import requests
from bs4 import BeautifulSoup


def Req(rates):
    rates2 = {}
    for elem in rates:
        if elem != None:
            url = 'https://www.tinkoff.ru/invest/currencies/' + elem + 'RUB/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html5lib')  # html5lib lxml lxml-xml
            quotes = soup.find_all('span', class_='Money-module__money_UZBbh')
            quot = quotes[0]
            rates2[elem] = quot.text[:len(quot.text) - 5]
    print("ok")
    return rates2
