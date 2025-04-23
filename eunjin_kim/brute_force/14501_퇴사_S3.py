'''
14501_퇴사_S3 #57

[1]알고리즘, 최악복잡도
완탐
[2]경계값, 히든테케
[3]슈도코드
'''

import sys
input = sys.stdin.readline


def dfs(depth, price):
  global max_price
  if depth == n:
    max_price = max(max_price, price)
    return

  if depth > n:
    return

  t, p = seq[depth]
  dfs(depth + t, price + p)
  dfs(depth + 1, price)


n = int(input())
seq = [list(map(int, input().split())) for _ in range(n)]

max_price = 0
dfs(0, 0)
print(max_price)