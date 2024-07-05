def final_merge(n_list, m_list):
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
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return final_merge(left, right)


inp = open('Lab 2/Task 2/input2.txt', 'r')
out = open('Lab 2/Task 2/output2.txt', 'w')

n = int(inp.readline().strip())
n_list = list(map(int, inp.readline().strip().split()))

m = int(inp.readline().strip())
m_list = list(map(int, inp.readline().strip().split()))

n_list= n_list+m_list

f_list = merge_sort(n_list)

print(' '.join(str(i) for i in f_list), file=out)

inp.close()
out.close()