print("CHECK FACTORIAL OF A GIVEN NUMBER :\n")
print()
num=int(input("PRINT THE NUMBER YOU WANT TO CHECK:\n"))
total=1
if num>=0:
    for fact in range (num,0,-1):
        total= total*fact
    print(f'The factorial of {num} is {total}')
else:
    print(f'The given number {num} is a negative number')