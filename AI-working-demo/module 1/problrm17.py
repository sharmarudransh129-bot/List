print("Code to check prime number :")
print()

num = int(input("Enter the number :"))

count = 0

for loop in range(2, (num//2) + 1, 1):
    if num % loop == 0:
        count = count + 1
        break

if count == 0 and num > 1:
    print(f"The given number {num} is a prime number")
else:
    print(f"The given number {num} is not a prime number")