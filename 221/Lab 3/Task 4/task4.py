def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def findKthSmallest(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_idx = partition(arr, low, high)
    if pivot_idx == k - 1:
        return arr[pivot_idx]
    elif pivot_idx > k - 1:
        return findKthSmallest(arr, low, pivot_idx - 1, k)
    else:
        return findKthSmallest(arr, pivot_idx + 1, high, k)

inp = open('Lab3/Task 4/input4.txt','r')
out = open('Lab3/Task 4/output4.txt','w')

n= int(inp.readline())
arr = list(map(int, inp.readline().strip().split()))
m = int(inp.readline())

for _ in range(m):
    k = int(inp.readline())
    kth_smallest = findKthSmallest(arr, 0, n - 1, k)
    print(kth_smallest, file=out)
