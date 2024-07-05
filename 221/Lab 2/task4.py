def find_max(arr, low, hi):
    if low == hi:
        return arr[low]

    mid = (low + hi) // 2

    l_arr = find_max(arr, low, mid)
    r_arr = find_max(arr, mid + 1, hi)

    return max(l_arr, r_arr)

inp = open('Lab 2\Task 4\input4.txt', 'r')
out = open('Lab 2\Task 4\output4.txt', 'w')

n = int(inp.readline().strip())
arr= list(map(int, inp.readline().strip().split()))

max_val = find_max(arr, 0, len(arr) - 1)
print(max_val, file=out)

out.close()

"""
The time complexity of the code id O(logn). Because the algorithm divide the array into half recursively.
It divides the array until its length become 1.
"""