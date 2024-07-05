def bfs(grph, strt, fin):
    queue = []
    visited = [False] * (len(grph) + 1)
    parent = [0] * (len(grph) + 1)

    queue.append(strt)
    visited[strt] = True

    while queue:
        current = queue.pop(0)

        for nhbr in grph[current]:
            if not visited[nhbr]:
                queue.append(nhbr)
                visited[nhbr] = True
                parent[nhbr] = current

    path = []
    while fin != strt:
        path.append(fin)
        fin = parent[fin]
    path.append(strt)

    return path[::-1]

inp = open('Lab 4/Task 5/input5.txt','r')
out = open('Lab 4/Task 5/output5.txt','w')

n, m, d = map(int, inp.readline().strip().split())

grph = {i: [] for i in range(1, n + 1)}
for i in range(m):
    u, v = map(int, inp.readline().strip().split())
    grph[u].append(v)
    grph[v].append(u)

shortest_path = bfs(grph, 1, d)
min_time = len(shortest_path) - 1

print("Time:", min_time, file=out)
print("Shortest Path:", *shortest_path,file=out)
