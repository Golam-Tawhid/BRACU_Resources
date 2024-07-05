from collections import defaultdict, deque

def bfs(course, graph, in_degree, order):
    queue = deque([course])

    while queue:
        cur = queue.popleft()
        if cur not in order:
            order.append(cur)

        for nxt in graph[cur]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)


def find_lexicographically_smallest(num, pre):
    graph = defaultdict(list)
    in_degree = [0] * (num + 1)

    for a, b in pre:
        graph[a].append(b)
        in_degree[b] += 1

    order = []
    for course in range(1, num + 1):
        if in_degree[course] == 0:
            bfs(course, graph, in_degree, order)
    if len(order) != num:
        return "IMPOSSIBLE"
    return order


inp = open('Lab 5/Task 2/input2.txt','r')
out = open('Lab 5/Task 2/output2.txt','w')

n, m = map(int, inp.readline().strip().split())

pre = []

for i in range(m):
    a= tuple(map(int, inp.readline().strip().split()))
    pre.append(a)

print(*find_lexicographically_smallest(n, pre), file=out)
