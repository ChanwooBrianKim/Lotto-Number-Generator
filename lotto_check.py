import requests
from bs4 import BeautifulSoup

# get lotto number from user
user_lotto = []
bonus_number = []
print('Enter your lotto number')
for i in range(6):
    lotto_num = input()
    user_lotto.append(int(lotto_num))

# get bonus number from user
print('Enter your bonus number')
bonus_num = input()
bonus_number.append(int(bonus_num))
    
# user whole lotto number list
user_result = [sorted(user_lotto), bonus_number]

# scrap actual lotto number
url = 'https://search.naver.com/search.naver?sm=tab_drt&where=nexearch&query=970회로또'
req = requests.get(url)

print(req)

html = BeautifulSoup(req.text, 'html.parser')
# gather 6 numbers except for bonus number (7th number)
num = html.select("span.num")
num_list = [int(i.text) for i in num]
del num_list[6]

# show bonus number separately
act_bonus = num[6]
bonus = [int(i.text) for i in num]
bonus_num = [bonus[6]]

actual_result = [num_list, bonus_num]
print(actual_result)

# check number with actual lotto number
if user_result[0] == actual_result[0]:
    print('You win')
else:
    print('Try again')
