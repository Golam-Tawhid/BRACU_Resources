def maximize_tasks(tasks, m):
    tasks.sort(key=lambda x: x[1])

    selected = [[] for j in range(m)]

    for i in tasks:
        for j in range(m):
            start, end = i

            if not selected[j] or start >= selected[j][-1][1]:
                selected[j].append((start, end))

                break

    return sum(len(task) for task in selected)


inp = open('Lab 7/Task 2/input2.txt','r')
out = open('Lab 7/Task 2/output2.txt','w')

n, m = map(int, inp.readline().strip().split())
tasks = []
for i in range(n):
    start, end = map(int, inp.readline().strip().split())
    tasks.append((start, end))

max_completed_tasks = maximize_tasks(tasks, m)
print(max_completed_tasks, file=out)