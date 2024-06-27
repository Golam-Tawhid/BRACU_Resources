maxVal = float('-inf')

def calculation(a,b):
    return [max(a) + max(b, key=abs)**2]

def findMaxVal(arr):
    global maxVal
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2
        a1 = findMaxVal(arr[:mid])
        a2 = findMaxVal(arr[mid:])
        # print(calculation(a1,a2),a1,a2)
        maxVal= max(maxVal, calculation(a1,a2)[0])
        return a1+a2

inp = open('Lab3/Task 2/input2.txt','r')
out = open('Lab3/Task 2/output2.txt','w')

n = int(inp.readline())
arr = list(map(int, inp.readline().strip().split()))

result = findMaxVal(arr)
print(maxVal, file=out)