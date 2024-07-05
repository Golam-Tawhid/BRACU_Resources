inp= open('Lab 2\Task 2\input2.txt','r')
out= open('Lab 2\Task 2\output2.txt','w')

n= inp.readline()
n_list=list(map(int, inp.readline().strip().split()))

m= inp.readline()
m_list=list(map(int, inp.readline().strip().split()))

i,j=0,0

f_list=[]

while i<int(n) and j<int(m):
    if n_list[i]==m_list[j]:
        f_list.append(n_list[i])
        f_list.append(m_list[j])
        i+=1
        j+=1
    elif n_list[i]<m_list[j]:
        f_list.append(n_list[i])
        i+=1
    else:
        f_list.append(m_list[j])
        j+=1

if i<int(n):
    f_list.extend(n_list[i:])

elif j<int(m):
     f_list.extend(m_list[j:])


print(' '.join(str(i) for i in f_list), file=out)
out.close()