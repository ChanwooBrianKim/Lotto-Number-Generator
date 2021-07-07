import requests
from bs4 import BeautifulSoup

for i in range(965,971):
    url = 'https://search.naver.com/search.naver?sm=tab_drt&where=nexearch&query={}회로또'.format(i)
    req = requests.get(url)

    print(req)

    html = BeautifulSoup(req.text, 'html.parser')
    num = html.select("span.num")
    num_list = [int(i.text) for i in num]
    print("{}회차".format(i), num_list)
