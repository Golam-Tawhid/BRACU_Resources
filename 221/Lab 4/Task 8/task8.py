def parentFind(parent, node):
    if parent[node] == node:
        return node
    parent[node] = parentFind(parent, parent[node])
    return parent[node]

def union_sets(parent, size, node1, node2):
    root1 = parentFind(parent, node1)
    root2 = parentFind(parent, node2)

    if root1 != root2:
        if size[root1] >= size[root2]:
            parent[root2] = root1
            size[root1] += size[root2]
        else:
            parent[root1] = root2
            size[root2] += size[root1]

inp = open('Lab 4/Task 8/input8.txt','r')
out = open('Lab 4/Task 8/output8.txt','w')
t = int(inp.readline())

for i in range(1, t + 1):
    n = int(inp.readline())
    parent = [i for i in range(2 * n + 1)]
    size = [1] * (2 * n + 1)

    for i in range(n):
        u, v = map(int, inp.readline().strip().split())
        union_sets(parent, size, u, v)

    max_members = max(size)

    print(f"Case {i}: {max_members}", file=out)