#7분
N = int(input())
whereToGo = list(input().split())

x, y = 1, 1
for i in whereToGo:
    if i == 'L':
        if x != 1:
            x -= 1
    elif i == 'R':
        if x != N:
            x += 1
    elif i == 'U':
        if y != 1:
            y -= 1
    elif i == 'D':
        if y != N:
            y+= 1

#dx = [0, 0, -1, 1]
#dy = [-1, 1, 0, 0]
#move_types = ['L', 'R', 'U', 'D']
#for toGo in whereToGo:
#    for i in range(len(move_types)):
#        if toGo == move_types[i]:
#            nx = x + dx[i]
#            ny = y + dy[i]
#    if nx < 1 or ny < 1 or nx > N or ny < N:
#        continue
#    x, y = nx, ny

print(y, x)