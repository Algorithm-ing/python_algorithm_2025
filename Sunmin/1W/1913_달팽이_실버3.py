N = int(input())
target = int(input())

lists = [[0] * N for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
way = [0, 1, 2, 3]  # 아래 → 오른쪽 → 위 → 왼쪽
way_num = 0

x = 0
y = 0
num = N * N

for i in range(num):
    lists[y][x] = num

    if num == target:
        target_pos = (y + 1, x + 1)

    num -= 1

    dir = way[way_num % 4]
    nx = x + dx[dir]
    ny = y + dy[dir]

    if not (0 <= nx < N and 0 <= ny < N) or lists[ny][nx] != 0:
        way_num += 1
        dir = way[(way_num) % 4]
        nx = x + dx[dir]
        ny = y + dy[dir]

    x, y = nx, ny

for row in lists:
    print(*row)
print(*target_pos)
