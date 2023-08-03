def addition(n1, n2):
  """add 2 numbers"""
  return n1 + n2

def subtract(n1, n2):
  """subtract n2 from n1"""
  return n1 - n2

def multiply(n1, n2):
  """multiply two numbers"""
  return n1 * n2

def divide(n1, n2):
  """divide n1 by n2"""
  return n1 / n2

operations = {
  "+": "addition",
  "-": "subtract",
  "*": "multiply",
  "/": "divide",
}

num1 = int(input("What's the first number: "))
for op in operations:
  print(op)
operation_symbol = input("Pick an operation from above: ")
num2 = int(input("What's the second number: "))
answer = locals()[operations[operation_symbol]](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
#do not understand locals() at all but it worked? lets you use a string to call a function
#but also OMG i got it in my operations dictionary I do NOT have to make the definitions strings...

'''
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
'''

#str object not callable, but I checked and operations[operation_symbol] makes a string? can't use a string to call a function?
#print(locals(operations[operation_symbol](num1, num2)))

'''
if operation_symbol == "+":
  index = 0
elif operation_symbol == "-":
  index = 1
elif operation_symbol == "*":
  index = 2
elif operation_symbol == "/":
  index = 3

listofoperations = ["addition", "subtract", "multiply", "divide"]
print(listofoperations[index](num1, num2))
'''
