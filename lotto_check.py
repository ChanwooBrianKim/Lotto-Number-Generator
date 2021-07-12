import requests
from bs4 import BeautifulSoup

# get the latest version of lotto result
print("Enter this week's version of lotto result")
this_week = input()

# get lotto number from user
user_lotto = []
bonus_number = 0
print('Enter your lotto number')
for i in range(6):
    lotto_num = input()
    user_lotto.append(int(lotto_num))

# get bonus number from user
print('Enter your bonus number')
user_bonus = input()
    
# user whole lotto number list
user_result = [sorted(user_lotto), int(user_bonus)]

# scrap actual lotto number
url = 'https://search.naver.com/search.naver?sm=tab_drt&where=nexearch&query={}회로또'.format(this_week)
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
bonus_num = bonus[6]

actual_result = [num_list, bonus_num]
print(actual_result)
print(user_result)

# check number with actual lotto number
# return result

def result():
    count = 0
    bonus_count = 0
    if actual_result[1] == user_result[1]:
        bonus_count += 1

    if actual_result[0] == user_result[0]:
        print('1st')
    elif actual_result[0] != user_result[0]:        
        for i in actual_result[0]:
            if i in user_result[0]:
                count += 1
        print(count)

        if count == 5 and actual_result[1] == user_result[1]:
            print('2nd')
        elif (count + bonus_count) == 5:
            print('3rd')
        elif (count + bonus_count) == 4:
            print('4th')
        elif (count + bonus_count) == 3:
            print('5th')
result()
