#Gemini answer
def calculate(num1, num2, operator):
  """Performs calculation based on the operator."""
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    if num2 == 0:
      return "Cannot divide by zero"
    return num1 / num2
  else:
    return "Invalid operator"

def main():
  """Main function to run the calculator."""

  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the next number: "))

  print("Select the operation:")
  operator = input("+  -  * /  \n")

  result = calculate(num1, num2, operator)
  print(f"Result of {num1} {operator} {num2} is {result}")

  continue_calc = input(f"Continue the operation with {result}? y/n: ")

  while continue_calc.lower() == 'y':
    num2 = int(input("Enter the next number: "))
    print("Select the operation:")
    operator = input("+  -  * /  \n")
    result = calculate(result, num2, operator)
    print(f"Result of {result-num2} {operator} {num2} is {result}")
    continue_calc = input(f"Continue the operation with {result}? y/n: ")

if __name__ == "__main__":
  main()