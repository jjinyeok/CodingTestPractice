#31분 - 답안 참고
#DFS/BFS part는 BOJ로라도 더 공부를 해야할듯함

from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(map(int, stdin.readline().strip())))

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N - 1][M - 1]

print(bfs(0,0))