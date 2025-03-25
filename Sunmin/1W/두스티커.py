h, w = map(int, input().split())
n = int(input())
stickers = [list(map(int, input().split())) for _ in range(n)]

ans = 0
area = 0
# print(stickers)

for i in range(n):
    for j in range(i + 1, n):
        r1 = stickers[i][0]
        c1 = stickers[i][1]
        r2 = stickers[j][0]
        c2 = stickers[j][1]

        area = r1 * c1 + r2 * c2
        # print(r1, c1, r2, c2)
        # print(area)

        # 돌리지 않고 옆에
        if r1 + r2 <= w and max(c1, c2) <= h:
            if ans < area:
                ans = area
        # 돌리지 않고 아래
        if c1 + c2 <= h and max(r1, r2) <= w:
            if ans < area:
                ans = area
        # 2돌리고 옆에
        if r1 + c2 <= w and max(c1, r2) <= h:
            if ans < area:
                ans = area
        # 2돌리고 아래
        if r1 + c2 <= h and max(c1, r2) <= w:
            if ans < area:
                ans = area
        # 1돌리고 옆에
        if c1 + r2 <= w and max(r1, c2) <= h:
            if ans < area:
                ans = area
        # 1돌리고 아래
        if c1 + r2 <= h and max(r1, c2) <= w:
            if ans < area:
                ans = area
        # 둘다돌리고 옆
        if c1 + c2 <= w and max(r1, r2) <= h:
            if ans < area:
                ans = area
        # 둘다돌리고 아래
        if r1 + r2 <= h and max(c1, c2) <= w:
            if ans < area:
                ans = area
print(ans)
