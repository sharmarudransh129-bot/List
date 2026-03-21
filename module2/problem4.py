print()
print("Code to Edit list:\n")
num=int(input("Enter the number  of elements in the list:\n"))
numbers=[]

for i in range(num):
    n=int(input(f"Enter the {i+1} element: "))
    numbers.append(n)
print(numbers)

org = numbers.copy()
print("\nSeperating Even and Odd Elements of the list:\n")
even=[]
odd=[]

for item in numbers:
    if item %2==0:
        even.append(item)
    else :
        odd.append(item)
print()
print(f"Even element lis: {even}")
print(f'Odd element list: {odd}')
print("The original list:")
print(numbers)
print("Rotating the list by 1 digit (left rotation):")

for i in range(num-1):
    numbers[i],numbers[i+1]=numbers[i+1],numbers[i]

print("The Rotated list is",numbers)
print()
numbers = org.copy()

print("Rotating the list by 1 digit (right rotation):")

last=numbers[-1]
for i in range (len(numbers)-1,0,-1):
    numbers[i]=numbers[i-1]
numbers[0]=last
print("The Rotated list is",numbers)

