import random

lotto_list = []
lotto_num = []
bonus_num = []

# 로또 전체 번호
for i in range(1, 46):
    lotto_list.append(i)

# 로또 5개 뽑기
for i in range(5):
    # 로또 번호 하나 뽑기
    lotto_one = random.randint(1,46)
    # 번호 겹치는지 검사
    if lotto_one in lotto_num:
        break
    else:
        lotto_num.append(lotto_one)

# 보너스 번호 뽑기
for i in range(1):
    special_one = random.randint(1,46)
    if special_one in lotto_num:
        break
    else:
        bonus_num.append(special_one)

if (len(lotto_num) == 5 and len(bonus_num) == 1):
    print(lotto_num, bonus_num)
else:
    print('retry')