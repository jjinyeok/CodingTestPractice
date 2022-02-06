# 5분
N, M = map(int, input().split())
results = []
for i in range(N):
    arr = list(map(int, input().split()))
    results.append(min(arr))
print(max(results))