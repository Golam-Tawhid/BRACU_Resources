def bfs(graph, start):
    visited = [False] * (len(graph) + 1)
    queue = []
    bfsPth = []

    queue.append(start)
    visited[start] = True

    while queue:
        vrtx = queue.pop(0)
        bfsPth.append(vrtx)

        for nhbr in graph[vrtx]:
            if not visited[nhbr]:
                queue.append(nhbr)
                visited[nhbr] = True

    return bfsPth


inp = open('Lab 4/Task 2/input2.txt', 'r')
out = open('Lab 4/Task 2/output2.txt', 'w')

n, m = map(int, inp.readline().strip().split())

graph = {i: [] for i in range(1, n + 1)}
for i in range(m):
    u, v = map(int, inp.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

bfs_result = bfs(graph, 1)
print(*bfs_result, file=out)