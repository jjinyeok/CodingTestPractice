#4분 오답
#0만 아니면 되는 경우가 아니라 두 수 중에서 하나라도 1 이하인 경우에는 더해야 함
#ex) 1 + 2 = 3, 1 * 2 = 2
from sys import stdin
input = stdin.readline

arr = list(map(int, input().rstrip()))
for i in range(len(arr) - 1):
    if arr[i] <= 1 or arr[i + 1] <= 1:
        arr[i + 1] = arr[i] + arr[i + 1]
#    오답(내 풀이)
#    if arr[i] == 0 or arr[i + 1] == 0:
#        arr[i + 1] = arr[i] + arr[i + 1]
    else:
        arr[i + 1] = arr[i] * arr[i + 1]

print(arr[len(arr) - 1])
