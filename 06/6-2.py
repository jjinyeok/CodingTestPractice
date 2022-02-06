# 3분
from sys import stdin

N = int(stdin.readline())
arr = []
for i in range(N):
    name, score = stdin.readline().split()
    arr.append([name, int(score)])

arr.sort(key=lambda x: x[1])
for i in range(N):
    print(arr[i][0], end=' ')
