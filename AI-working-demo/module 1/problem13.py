print("Code for LCM of two number:\n")
print()
num1=int(input("Enter first number :\n"))
num2=int(input('Enter second number :\n'))
maximum=max(num1,num2)
for loop in range (maximum,(num1*num2)+1,1):
    if loop %num1==0  and loop%num2==0:
        lcm=loop
        break
print(f'the lcm of {num1} and {num2} is {lcm}')