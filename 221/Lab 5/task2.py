import heapq

def lexicographically_smallest(num, pre):
    graph = {i: [] for i in range(1, num + 1)}
    in_degree = [0] * (num + 1)

    for a, b in pre:
        graph[a].append(b)
        in_degree[b] += 1

    heap = [i for i in range(1, num + 1) if in_degree[i] == 0]
    heapq.heapify(heap)

    order = []
    while heap:
        current = heapq.heappop(heap)
        order.append(current)

        for nxt in graph[current]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                heapq.heappush(heap, nxt)

    if len(order) == num:
        return order
    else:
        return "IMPOSSIBLE"

inp = open('Lab 5/Task 2/input2.txt','r')
out = open('Lab 5/Task 2/output2.txt','w')

n, m = map(int, inp.readline().strip().split())

pre = []

for i in range(m):
    a= tuple(map(int, inp.readline().strip().split()))
    pre.append(a)

print(*lexicographically_smallest(n, pre), file=out)