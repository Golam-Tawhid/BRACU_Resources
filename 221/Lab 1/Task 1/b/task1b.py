def calculator(exp):
    word, operand1, operator, operand2 = exp.split(" ")
    operand1 = int(operand1)
    operand2 = int(operand2)
  
    if operator == '+':
      print(f"The result of {operand1} {operator} {operand2} is {operand1 + operand2}", file=out)
    elif operator == '-':
      print(f"The result of {operand1} {operator} {operand2} is {operand1 - operand2}", file=out)
    elif operator == '*':
      print(f"The result of {operand1} {operator} {operand2} is {operand1 * operand2}", file=out)
    elif operator == '/':
      print(f"The result of {operand1} {operator} {operand2} is {operand1 / operand2}", file=out)
      
inp=open('Lab 1/Task 1/b/input1b.txt','r')
out=open('Lab 1/Task 1/b/output1b.txt','w')

n=int(inp.readline())

for i in range(n):
  result= calculator(inp.readline())

out.close()