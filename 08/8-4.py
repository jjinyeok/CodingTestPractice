# 21분 내 풀이랑 답안이 많이 다르나 반례를 찾지 못하였음
from sys import stdin
N, M = map(int, stdin.readline().split())
coins = [int(stdin.readline()) for _ in range(N)]
coins.sort(reverse=True)

money = [-1] * 10001
for coin in coins:
    money[coin] = 1

for i in range(1, M + 1):
    for coin in coins:
        if money[i - coin] != -1:
            money[i] = money[i - coin] + 1
            break

print(money[M])

#답안
d = [10001] * (M + 1)
d[0] = 0
for i in range(N):
    for j in range(coins[i], M + 1):
        if d[j - coins[i]] != 10001:
            d[j] = min(d[j], d[j - coins[i]] + 1)
if d[M] == 10001:
    print(-1)
else:
    print(d[M])