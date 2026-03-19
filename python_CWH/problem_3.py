print("Code to perform arithmetic calculation on given two numbers:\n")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nOperation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

oper = int(input("Enter the operation (1-4): "))

if oper == 1:
    result = num1 + num2
elif oper == 2:
    result = num1 - num2
elif oper == 3:
    result = num1 * num2
elif oper == 4:
    result = num1 / num2
else:
    print("Invalid operation")
    result = None

if result is not None:
    print(f"\nThe answer of operation on {num1} and {num2} is {result}")