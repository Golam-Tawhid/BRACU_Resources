#Task 3
def selection_sort(ids, marks):
  for i in range(len(ids)):
    min_idx=i
    for j in range(i+1, len(ids)):
      if marks[j] > marks[min_idx]:
        min_idx = j
      elif marks[j] == marks[min_idx] and ids[j] < ids[min_idx]:
        min_idx = j
    marks[i], marks[min_idx] = marks[min_idx], marks[i]
    ids[i], ids[min_idx] = ids[min_idx], ids[i]

  return ids, marks

inp=open('Lab 1/Task 3/input3.txt','r')
output_file=open('Lab 1/Task 3/output3.txt','w')

n=int(inp.readline())
id = list(map(int, inp.readline().strip().split()))
mrk = list(map(int, inp.readline().strip().split()))

id, mrk = selection_sort(id, mrk)

for i in range(n):
  print(f"ID: {id[i]} Mark: {mrk[i]}", file=output_file)


output_file.close()