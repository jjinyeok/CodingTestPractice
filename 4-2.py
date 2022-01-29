#12분
count_not_3 = 0

for i in range(60):
    for j in range(60):
        min_sec = str(i)+str(j)
        if min_sec.find('3') != -1:
            count_not_3 += 1

count_in_3 = 60 * 60

N = int(input())
if N < 3:
    result = count_not_3 * (N + 1)
elif N < 13:
    result = count_not_3 * N + count_in_3
elif N < 23:
    result = count_not_3 * (N - 1) + count_in_3 * 2
elif N == 23:
    result = count_not_3 * (N - 2) + count_in_3 * 3

#count = 0
#for i in range(N + 1):
#    for j in range(60):
#        for k in range(60):
#            if '3' in str(i) + str(j) + str(k):
#                count += 1

print(result)