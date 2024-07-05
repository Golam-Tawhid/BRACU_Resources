count=0
def divide(arr):
    if len(arr)<=1:
        return arr
    else:
        mid= len(arr)//2
        arr1 = divide(arr[:mid])
        arr2 = divide(arr[mid:])
        # print(arr1,arr2)
        return solution(arr1, arr2)

def solution(arr1, arr2):
    global count
    i, j= 0,0
    fin=[]
    while i<len(arr1) or j<len(arr2):
        print(i,j,arr1,arr2)
        if i>= len(arr1):
            fin.extend(arr2[j:])
            j+=len(arr2)

        elif j>= len(arr2):
            fin.extend(arr1[i:])
            # count+=1
            i+=len(arr1)
        
        
        else:
            if arr1[i] < arr2[j]:
                fin.append(arr1[i])
                i+=1

            else:
                fin.append(arr2[j])
                count+=len(arr1)-i
                j+=1
        print(fin, count)

    return fin







inp = open('Lab3/Task 1/input1.txt','r')
out = open('Lab3/Task 1/output1.txt','w')

n= int(inp.readline())
arr = list(map(int, inp.readline().strip().split()))

final= divide(arr)

print(final)
print(count, file=out)