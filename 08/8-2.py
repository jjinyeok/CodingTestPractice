#18분 풀긴했는데 더 쉬운 방법이 존재(앞부터 풀어도 됐었는데)
from sys import stdin
N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

#d = [0] * 100
#d[0] = arr[0]
#d[1] = max(arr[0], arr[1])
#for i in range(2, N):
#    d[i] = max(d[i - 1], d[i - 2] + arr[i])
#print(d[N - 1])

result = [0] * (N)
result[N - 1] = arr[N - 1]
result[N - 2] = max(arr[N - 2], arr[N - 1])
tmp = 0
for i in range(N - 2, -1, -1):
    for j in range(i + 2, N):
        if tmp < result[j]:
            tmp = result[j]
    result[i] = tmp + arr[i]

print(max(result))
