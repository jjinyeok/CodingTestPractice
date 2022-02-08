#16분
from sys import stdin
input = stdin.readline

S = list(input().rstrip())
S.sort()

find = len(S)
for i in range(len(S)):
    if ord(S[i]) > ord('9'):
        find = i
        break

alphabet = S[find:]
number = sum(list(map(int, S[:find])))

result = alphabet
print(''.join(result), end='')
print(number)
