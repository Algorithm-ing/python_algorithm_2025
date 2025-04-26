'''
[1]알고리즘, 최악복잡도
bfs 연산의 최솟값을 구하는 문제이므로 dfsXX
[2]경계값, 히든테케
- -1 출력
- 1,000,000,000 < 2^30 -> int 정수최댓값 2^32-1 -> ok
[3]슈도코드
'''

import sys 
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque([(start, 1)])

    while q:
        x, cnt = q.popleft()
        y, z = x * 2, int(str(x) + '1')
        cnt += 1

        if y == target or z == target:
            return cnt
        if y < target:
            q.append((y, cnt))
        if z < target:
            q.append((z, cnt))

    return -1


n, target = map(int, input().split())
print(bfs(n))