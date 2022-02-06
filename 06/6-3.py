# 8분
from sys import stdin

N, K = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[0] < B[0]:
        A[0], B[0] = B[0], A[0]
        A.sort()
        B.sort(reverse=True)

#for i in range(K):
#    if A[i] < B[i]:
#        A[i], B[i] = B[i], A[i]
#    else:
#        break

print(sum(A))