print()
print("Code to make a list for given number of Elements")
print()
num=int(input("Enter the number of Elements in the list:\n"))
number=[]
for elements in range(num):
    n=int(input(f"Enter the {elements+1} number: "))
    number.append(n)

print("Number in the list:\n",number)

print()
print("First and Last element of list:\n")
print(f"First :  {number[0]}")
print(f"Last  :  {number[num-1]}")
print()

change=int(input('Enter the elemnt you want to change:\n'))
print(f"The element in the list to be changed :{number[change-1]}")
num2=int(input('Enter the changed Second Element of list: '))
number[change-1]=num2
# print(f'The second elemnt in the list after changing: {number[change-1]}')
print(number)
print()
add1=int(input("Enter the first element you want to add:\n"))
number.append(add1)
add2=int(input("Enter the second element you want to add:\n"))
number.append(add2)
print()
print(number)
print()
print(f"The length of the given list is {len(number)}")