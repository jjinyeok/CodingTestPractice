#22분 답안 참고
from sys import stdin
arr = [0] * 30001
X = int(stdin.readline())

for i in range(2, X + 1):
    arr[i] = arr[i - 1] + 1
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i // 2] + 1)
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i // 3] + 1)
    if i % 5 == 0:
        arr[i] = min(arr[i], arr[i // 5] + 1)

print(arr[X])