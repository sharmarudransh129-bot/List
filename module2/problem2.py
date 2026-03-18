print()
print("Code to perform operations on list")
print()
num=int(input("Enter the number of elements in the list: "))
numbers=[]
for elements in range(num):
     n=int(input(f"Enter the {elements+1} number: "))
     numbers.append(n)
print()
print(numbers)
print()
num1=int(input("Enter the 1st number you want to add: "))
num2=int(input("Enter the 2nd number you want to add: "))
print()
sum=numbers[num1-1]+numbers[num2-1]
print(f"the sum of {numbers[num1-1]} and {numbers[num2-1]} is {sum}")
print()
print("the maximum and minimum value of elements in the list is :")
print(numbers)
print(f"Maximum number: {max(numbers)}")
print(f'Minimum number: {min(numbers)}')
      
print()
count=0
for add in range (num):
     if (numbers[add]%2==0):
         count+=1
print("The number of even numbers in the list",count)
print()
rev=[]
for j in range(len(numbers)-1,-1,-1):
    rev.append(numbers[j])
print(f"rev of List: {rev}")
#print("\nCode to perform operations on list\n")

# num = int(input("Enter number of elements: "))
# numbers = []

# for i in range(num):
#     n = int(input(f"Enter element {i+1}: "))
#     numbers.append(n)

# print("\nList:", numbers)

# if not numbers:
#     print("List is empty. Exiting...")
# else:
#     # Safe index input
#     pos1 = int(input("Enter position of 1st element: "))
#     pos2 = int(input("Enter position of 2nd element: "))

#     if 1 <= pos1 <= num and 1 <= pos2 <= num:
#         total = numbers[pos1-1] + numbers[pos2-1]
#         print(f"Sum = {total}")
#     else:
#         print("Invalid positions!")

#     print("\nMaximum:", max(numbers))
#     print("Minimum:", min(numbers))

#     # Even count (Pythonic)
#     count = 0
#     for n in numbers:
#         if n % 2 == 0:
#             count += 1

#     print("Even numbers count:", count)