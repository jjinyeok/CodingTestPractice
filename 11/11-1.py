#20분
#풀이 과정 자체는 맞았으나, 깔끔한 코드를 못짰음
#굳이 리스트나 큐를 쓰지 않았어도 됐던 문제
from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))

result = 0
arr.sort()
while True:
    count = arr[0]
    result += 1
    for i in range(count):
        if len(arr) == 0:
            break
        pop = arr.pop(0)
        if pop != count:
            count = pop
    if len(arr) == 0:
        break

print(result - 1)

#result = 0
#count = 0
#for i in arr:
#    count += 1
#    if count >= i:
#        result += 1
#        count = 0
#print(result)
