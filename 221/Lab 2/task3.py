def merge(n_list, m_list):
    i, j = 0, 0
    f_list = []

    while i < len(n_list) and j < len(m_list):
        if n_list[i] <= m_list[j]:
            f_list.append(n_list[i])
            i += 1
        else:
            f_list.append(m_list[j])
            j += 1

    f_list.extend(n_list[i:])
    f_list.extend(m_list[j:])

    return f_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    l_arr = merge_sort(arr[:mid])
    r_arr = merge_sort(arr[mid:])
    return merge(l_arr, r_arr)


inp = open('Lab 2\Task 3\input3.txt', 'r')
out = open('Lab 2\Task 3\output3.txt', 'w')

n = int(inp.readline().strip())
arr= list(map(int, inp.readline().strip().split()))

f_list = merge_sort(arr)

print(' '.join(str(i) for i in f_list), file=out)

out.close()