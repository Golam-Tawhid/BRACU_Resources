def maximize_tasks(tasks, M):
    tasks.sort(key=lambda x: x[1])  # Sort tasks by end time
    completed_tasks = 0
    end_times = [0] * M
    c=0

    for task in tasks:
        c+=1
        start, end = task
        assigned = False

        for i in range(M):
            if end_times[i] <= start:
                end_times[i] = end
                completed_tasks += 1
                assigned = True
                break
        
        if c==len(tasks):
            M-=1
            tsk= maximize_tasks(tasks[1:],M)
            count+=tsk
    
    return completed_tasks

# Read input
N, M = map(int, input().split())
tasks = []
for _ in range(N):
    start, end = map(int, input().split())
    tasks.append((start, end))

# Find and print the maximum number of activities that can be completed
result = maximize_tasks(tasks, M)
print(result)
