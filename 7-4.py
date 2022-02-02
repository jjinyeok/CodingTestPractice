#8분
from sys import stdin
N = int(stdin.readline())
elements = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
targets = list(map(int, stdin.readline().split()))

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
    return None

elements.sort()
for target in targets:
    result = binary_search(elements, target, 0, N - 1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')

#계수 정렬 개념 이용
#array = [0] * 1000001
#for i in stdin.readline().split():
#    array[int(i)] = 1
#targets = list(map(int, stdin.readline().split()))
#for target in targets:
#    if array[target] == 1:
#        print('yes', end=' ')
#    else:
#        print('no', end=' ')

#set 자료형 이용
#array = set(map(int, input().split()))
#for target in targets:
#    if target in array:
#        print('yes', end=' ')
#    else:
#        print('no', end=' ')