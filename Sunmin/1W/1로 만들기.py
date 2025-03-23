X = int(input())
dp = [0] * (X + 1)
lists = [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]

if X < 10 :
    for i in range(X+1):
        dp[i] = lists[i]
else:
    for i in range(11):
        dp[i] = lists[i]

if X < 10:
    print(dp[X])
    quit()

for i in range(10, X + 1):

    min_lists = []

    if i % 3 == 0:
        min_lists.append(dp[i // 3] + 1)

    if i % 2 == 0:
        min_lists.append(dp[i // 2] + 1)

    min_lists.append(dp[i - 1] + 1)

    dp[i] = min(min_lists)

#     print(i)
#     print(dp)
# print(dp)
# print(num)
# print(dp)
print(dp[X])
# [0, 1, 1, 2, 3, 2, 3, 3, 2, 3, 4, 3, 4, 4, 4, 4, 5, 3, 4, 4, 5]
