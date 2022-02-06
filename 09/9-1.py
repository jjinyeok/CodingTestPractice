from sys import stdin
input = stdin.readline
INF = 987654321

N, M = map(int, input().split())
start = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def find_short_distance():
    min = INF
    index = 0
    for i in range(1, N + 1):
        if distance[i] < min and visited[i] == False:
            min = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(N - 1):
        now = find_short_distance()
        visited[now] = True
        for j in graph[now]:
            if distance[j[0]] > distance[now] + j[1]:
                distance[j[0]] = distance[now] + j[1]

dijkstra(start)

for i in range(1, N + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])