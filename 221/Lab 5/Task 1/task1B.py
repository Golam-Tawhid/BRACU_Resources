def bfs(num, pre):
    graph = {i: [] for i in range(1, num + 1)}
    in_degree = [0] * (num + 1)

    for a, b in pre:
        graph[b].append(a)
        in_degree[a] += 1

    queue = []
    for course in range(1, num + 1):
        if in_degree[course] == 0:
            queue.append(course)

    order = []
    while queue:
        course = queue.pop(0)
        order.append(course)

        for nxt in graph[course]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    if len(order) != num:
        return "IMPOSSIBLE"

    return order[::-1]


inp = open('Lab 5/Task 1/input1b.txt','r')
out = open('Lab 5/Task 1/output1b.txt','w')

n, m = map(int, inp.readline().strip().split())

pre = []

for i in range(m):
    a= tuple(map(int, inp.readline().strip().split()))
    pre.append(a)

print(*bfs(n, pre), file=out)