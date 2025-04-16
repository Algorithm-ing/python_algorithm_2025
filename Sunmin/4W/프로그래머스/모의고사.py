def solution(answer):

    ans = []
    lists_1 = [1, 2, 3, 4, 5]
    lists_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    lists_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = {1: 0, 2: 0, 3: 0}

    for i in range(len(answer)):
        if lists_1[i % len(lists_1)] == answer[i]:
            score[1] += 1
    for i in range(len(answer)):
        if lists_2[i % len(lists_2)] == answer[i]:
            score[2] += 1
    for i in range(len(answer)):
        if lists_3[i % len(lists_3)] == answer[i]:
            score[3] += 1

    score = sorted(score.items(), key=lambda x: x[1], reverse=True)

    for key, value in score:
        if value == score[0][1]:
            ans.append(key)

    return ans

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))