from collections import deque

computer = int(input())
node = int(input())
queue = deque()
graph = []
ans = 0

visted = [False] * (computer + 1)
visted[1] = True
queue.append(1)

for _ in range(computer + 1): graph.append([])
for _ in range(node):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

while queue:

    NOW = queue.popleft()

    for i in graph[NOW]:
        if visted[i] == False:
            visted[i] = True
            queue.append(i)
            ans += 1

print(ans)
