#Task 2
def bubbleSort(arr):
  swap=False                                                  
  for i in range(len(arr)-1):
    swap=False
    for j in range(len(arr)-i-1): 
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swap=True

    if swap==False:
      break

"""
For the best-case scenario the array will be already sorted.
Here, swap is keeping track of swaps that were made during a pass through the array.
If no swaps are made during a pass, it means that the array is already sorted.
It will end the programme early and the time-complexity will be θ(n). 
"""

inp=open('Lab 1/Task 2/input2.txt','r')
out=open('Lab 1/Task 2/output2.txt','w')

n=int(inp.readline())
arr = list(map(int, inp.readline().strip().split()))
result=bubbleSort(arr)

for i in range(n):
  print(arr[i], end=" ", file=out)

out.close()