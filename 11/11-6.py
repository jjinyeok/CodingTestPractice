#27분 오답
#greedy 하게 풀 수 있는 방법이 있었음에도 생각하지 못 하였음
#정확성: 28.1
#효율성: 0.0
#합계: 28.1 / 100.0
#많은 문제를 접해봐야겠음
#책 다 끝내고 한번 더 풀어봐야지
def solution(food_times, k):
    if sum(food_times) <= k:
            return -1
    timer = 0
    count = 0
    while True:  
        if food_times[count % len(food_times)] > 0:
            food_times[count % len(food_times)] -= 1
            timer += 1
        count += 1
        if timer == k:
            answer = (count % len(food_times)) + 1
            return answer

#답안
import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
        #(음식 시간, 음식 번호)의 형태로 우선순위 큐에 삽입
    
    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    answer = result[(k - sum_value) % length][1]
    return answer
