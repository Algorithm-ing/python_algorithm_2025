# 15787 기차가 어둠을 헤치고 은하수를
import sys

N, M = map(int, sys.stdin.readline().split())

seats = [[0] * 20 for _ in range(N)]
print(seats)
for _ in range(M):
    command = sys.stdin.readline().split()
    type = int(command[0])
    if type == 1:
        if seats[command[1]][command[2]]:
            seats[command[1]][command[2]] = 1
    elif type == 2:
        if not seats[command[1]][command[2]]:
            seats[command[1]][command[2]] = 0
    elif type == 3:
        for i in range(20, -1):
            seats[command[1]][i+1] = seats[command[1]][i]

print(seats)
