#11분
#답안과는 다르지만 나도 맞게 짠듯
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
balls = [0] * 10
for i in arr:
    balls[i - 1] += 1
result = N * (N - 1) // 2

for i in balls:
    result -= i * (i - 1) // 2
print(result)

#답안
result = 0
for i in range(M):
    N -= balls[i]
    result += balls[i] * N
print(result)
