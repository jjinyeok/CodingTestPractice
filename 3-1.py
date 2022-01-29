# 11분
N = int(input())

money = [500, 100, 50, 10]
count = 0
what_money = 0
while N != 0:
    count += N // money[what_money]
    N %= money[what_money]
    what_money += 1

#for coin in money:
#    count += N //coin
#    N %= coin

print(count)
