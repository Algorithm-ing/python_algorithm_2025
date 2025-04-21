# 16953 A -> B
import sys

A, B = map(int, sys.stdin.readline().split())

cnt = 1
while B != A:
    if B % 2 == 0:  # 2로 나누어질 때
        B = B // 2
    elif B % 10 == 1:  # 뒷자리가 1로 끝날 때
        B = B // 10
    else:  # 아무 연산도 안될 경우
        cnt = -1
        break
    cnt += 1

    if B == 0:  # A를 B로 만들 수 없을 때
        cnt = -1
        break

print(cnt)
