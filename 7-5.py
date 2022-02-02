#50분 (아예 틀림 => 답지 참고)
#Parametric Search 유형 공부해야 할듯
from sys import stdin
N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in arr:
        if i - mid >= 0:
            total += (i - mid)
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
