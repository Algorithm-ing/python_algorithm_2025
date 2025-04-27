# 정확성: 74.2
# 효율성: 16.1
# 합계: 90.3 / 100.0
# import heapq
# def solution(scoville, K):
#     answer = 0
#     heapq.heapify(scoville)
#     while len(scoville) > 1:
#         min1 = heapq.heappop(scoville)
#         if min1 >= K:
#             break
#         min2 = heapq.heappop(scoville)

#         scoville.append(min1 + min2 * 2)
#         answer += 1

#     if scoville[0] < K:
#         return -1
#     return answer
