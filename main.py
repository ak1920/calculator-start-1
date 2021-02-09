def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1, n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations={
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1=int(input('Whats the first number?'))
num2=int(input('Whats the second number?'))

operation_fun=operations[]

op = input('pick an operation please')
print(f'{num1}{op}{num2}={answer}')