def maximize_tasks(tasks):
    tasks.sort(key=lambda x: x[1])
    selected = []
    prev_end = -1

    for i in tasks:
        start, end = i
        if start >= prev_end:
            selected.append(i)
            prev_end = end

    return selected

inp = open('Lab 7/Task 1/input1.txt','r')
out = open('Lab 7/Task 1/output1.txt','w')

n = int(inp.readline())
tasks = []
for i in range(n):
    start, end = map(int, inp.readline().strip().split())
    tasks.append((start, end))

selected = maximize_tasks(tasks)
print(len(selected), file=out)
for i in selected:
    print(i[0], i[1], file=out)