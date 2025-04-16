from itertools import permutations


def solution(numbers):
    ans = []

    # 소수 판별 함수
    def prime(num):

        for i in range(2, num):
            if num % i == 0:
                return

        return ans.append(num)

    lists = []
    all_num = []
    for i in numbers:
        lists.append(i)

    for i in range(1, len(lists) + 1):
        per_lists = permutations(lists, i)

        for p in per_lists:
            num = int(''.join(p))
            all_num.append(num)

    all_num = set(all_num)
    # print(all_num)

    for i in all_num:
        prime(i)

    # print(ans)
    if 1 in ans:
        ans.remove(1)
    if 0 in ans:
        ans.remove(0)

    # print(ans)

    return len(ans)


print(solution("17"))
print(solution("011"))