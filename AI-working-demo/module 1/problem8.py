print("CHECK WETHER THE NUMBER IS EVEN OR ODD:")
print()
num=int(input('Enter the number you want to check:'))
if num >=0:
    if num%2==0:
        print(f"The given number {num} is even number")
    else:
        print(f"The given number {num} is odd number")
else:
    print(f"The given number is negative number")