from art import logo
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

# reference to the function
operations = {
  "+": addition,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  another = True
  num1 = float(input("What's the first number: "))
  for op in operations:
    print(op)
  while another:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number: "))
    answer = operations[operation_symbol](num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    check_another = input(f"Type 'y' to continue calculating with {answer}: ").lower()
    if check_another == "y":
      num1 = answer
    else:
      another = False
      calculator()


calculator()
