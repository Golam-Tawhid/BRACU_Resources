def dfs(crs, graph, visited, stack):
    if visited[crs] == 1:
        return False
    if visited[crs] == 2:
        return True

    visited[crs] = 1

    for nxt in graph[crs]:
        if not dfs(nxt, graph, visited, stack):
            return False

    visited[crs] = 2
    stack.append(crs)
    return True


def find_order(num, pre):
    graph = {i: [] for i in range(1, num + 1)}
    for a, b in pre:
        graph[a].append(b)

    visited = [0] * (num + 1)
    stack = []

    for crs in range(1, num + 1):
        if not visited[crs]:
            if not dfs(crs, graph, visited, stack):
                return "IMPOSSIBLE"

    return stack[::-1]


inp = open('Lab 5/Task 1/input1a.txt','r')
out = open('Lab 5/Task 1/output1a.txt','w')

n, m = map(int, inp.readline().strip().split())

pre = []

for i in range(m):
    a= tuple(map(int, inp.readline().strip().split()))
    pre.append(a)

print(*find_order(n, pre), file=out)