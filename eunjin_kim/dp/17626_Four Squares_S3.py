'''
17626_Four Squares_S3 #54
pypy3 제출

[1]알고리즘, 최악복잡도
DP
'''

import sys 
sys.stdin = open("제출전삭제.txt","rt") 
input = sys.stdin.readline

n = int(input())
dp = [4] * (n+1)

for x in range(1, n+1):
    if x ** 2 <= n:
        dp[x**2] = 1

    if dp[x] == 1:
        continue

    for y in range(int(x ** 0.5), 0, -1):
        dp[x] = min(dp[x], dp[y**2] + dp[x - y**2])
    
print(dp[n])