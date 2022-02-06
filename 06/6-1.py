# 2분
from sys import stdin

N = int(stdin.readline())
arr = []
for i in range(N):
    arr.append(int(stdin.readline()))

arr.sort(key=lambda x: -x)
#arr.sort(reverse=True)

print(' '.join(map(str, arr)))
