#8분
from sys import stdin
input = stdin.readline

arr = list(input().rstrip())
zero_count = 0
one_count = 0
if arr[0] == '0':
    zero_count += 1
elif arr[0] == '1':
    one_count += 1

for i in range(1, len(arr)):
    if arr[i] != arr[i - 1]:
        if arr[i] == '0':
            zero_count += 1
        elif arr[i] == '1':
            one_count += 1

print(min(zero_count, one_count))
