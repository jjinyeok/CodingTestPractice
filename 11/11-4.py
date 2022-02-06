#30분 포기
#아이디어를 떠올리지 못했음
#그리디 알고리즘 유형의 문제를 여러 번 풀어보자
from sys import stdin
input = stdin.readline

N = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for x in coins:
    #만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

print(target)
#taget은 지금까지 동전들의 합이고, 이 합 안에 있는 모든 금액은 만들 수 있음
#1 1 2 3 9에서
#2까지, 4까지, 7까지의 모든 금액을 만들 수 있었음
#-> target(8) < 9가 되었을 때 종료
