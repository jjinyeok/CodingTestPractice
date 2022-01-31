#33분 - 답안 참고

from sys import stdin
N, M = map(int, stdin.readline().split())
graph = []
for i in range(N):
    arr = list(map(int, stdin.readline().strip()))
    graph.append(arr)

def dfs(x, y):
    if x < 0 or y < 0 or x > N - 1 or y > M -1:
        return False
    else:
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
        else:
            return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)