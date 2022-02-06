#29분
N, M = map(int, input().split())
A, B, d = map(int, input().split())
world = []
for i in range(N):
    world.append(list(map(int, input().split())))

result = 0
while True:
    if world[A - 1][B] != 0 and world[A+1][B] != 0 and world[A][B - 1] != 0 and world[A][B + 1] != 0:
        if d == 0:
            if world[A + 1][B] == 1:
                break
            elif world[A + 1][B] == 2:
                A = A + 1
                continue
        elif d == 1:
            if world[A][B - 1] == 1:
                break
            elif world[A][B - 1] == 2:
                B = B - 1
                continue
        elif d == 2:
            if world[A - 1][B] == 1:
                break
            elif world[A - 1][B] == 2:
                A = A - 1
                continue
        elif d == 3:
            if world[A][B + 1] == 1:
                break
            elif world[A][B + 1] == 2:
                B = B + 1
                continue
    if d == 0:
        d = 3
        if world[A][B - 1] == 0:
            B = B - 1
            world[A][B] = 2
            result += 1
        continue
    elif d == 1:
        d = 0
        if world[A - 1][B] == 0:
            A = A - 1
            world[A][B] = 2
            result += 1
        continue
    elif d == 2:
        d = 1
        if world[A][B + 1] == 0:
            B = B + 1
            world[A][B] = 2
            result += 1
        continue
    elif d == 3:
        d = 2
        if world[A + 1][B] == 0:
            A = A + 1
            world[A][B] = 2
            result += 1
        continue

print(result)