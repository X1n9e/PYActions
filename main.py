am = 0

def add_numbers(a, b):
      return a + b
print("Simple Calculator - Addition")
print("============================")
while am == 0:        
        # Input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
        
        # Perform addition
    result = add_numbers(num1, num2)
        
        # Output the result
    print(f"Result: {num1} + {num2} = {result}")
