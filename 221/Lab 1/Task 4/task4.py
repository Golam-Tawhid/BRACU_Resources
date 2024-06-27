#Task 4
def bubbleSort(train_info):
  n = len(train_info)
    
  for i in range(n - 1):
    for j in range(n - i - 1):
      name, w, x, y, loc, z, tm  = train_info[j].split(" ")
      hr, mn=tm.split(":")
      time=int(hr)*60+int(mn)
    
      nxt_name, a, b, c, nxt_loc, d, nxt_tm = train_info[j + 1].split(" ")
      nxt_hr, nxt_min=nxt_tm.split(":")
      nxt_time=int(nxt_hr)*60+int(nxt_min)
            
      if name > nxt_name:
        train_info[j], train_info[j + 1] = train_info[j + 1], train_info[j]
      elif name == nxt_name and time < nxt_time:
        train_info[j], train_info[j + 1] = train_info[j + 1], train_info[j]
  return train_info

inp=open('Lab 1/Task 4/input4.txt','r')
output_file=open('Lab 1/Task 4/output4.txt','w')

n=int(inp.readline())
train_info = []

for i in range(n):
  train_info.append(inp.readline().strip())

sorted_train_info = bubbleSort(train_info)

for j in sorted_train_info:
  print(j, file=output_file)

output_file.close()