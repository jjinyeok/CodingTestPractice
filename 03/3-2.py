# 14분
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr_tmp = arr
max_value = max(arr_tmp)
arr_tmp.pop(arr_tmp.index(max_value))
second_value = max(arr_tmp)
#arr.sort()
#max_value = arr[N - 1] #가장 큰 수
#second_value = arr[N - 2] #두 번째로 큰 수

#반복문을 사용하는 방법
#while True:
#    for i in range(K):
#        if m == 0:
#            break
#        result += max_value
#        m -= 1
#    if m == 0:
#        break
#    result += second
#    m -= 1

#반복되는 수열을 파악하는 방법
how_many1 = M // (K + 1)
how_many2 = M % (K + 1)
result = how_many1 * (max_value * K + second_value) + how_many2 * (max_value)

print(result)