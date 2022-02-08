#7분
from sys import stdin
input = stdin.readline

score = list(input().rstrip())
score = list(map(int, score))
if sum(score[:len(score) // 2]) == sum(score[len(score) // 2:]):
    print('LUCKY')
else:
    print('READY')
