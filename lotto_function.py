import requests
from bs4 import BeautifulSoup

# get lotto number from user
user_lotto = []
print('Enter your lotto number')
for i in range(7):
    lotto_num = input()
    user_lotto.append(lotto_num)
    
print(user_lotto)

# scrap actual lotto number
for i in range(965,971):
    url = 'https://search.naver.com/search.naver?sm=tab_drt&where=nexearch&query={}회로또'.format(i)
    req = requests.get(url)

    print(req)

    html = BeautifulSoup(req.text, 'html.parser')
    num = html.select("span.num")
    num_list = [int(i.text) for i in num]
    print("{}회차".format(i), num_list)
