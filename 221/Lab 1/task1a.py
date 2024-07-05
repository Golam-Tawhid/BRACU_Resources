inp=open('Lab 1/Task 1/a/input1a.txt','r')
out=open('Lab 1/Task 1/a/output1a.txt','w')

n=int(inp.readline())

for i in range(n):
  num=int(inp.readline())

  if num%2==0:
    print(f"{num} is an Even number",file=out)
  else:
    print(f"{num} is an Odd number",file=out)

out.close()