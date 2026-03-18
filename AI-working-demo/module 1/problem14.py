print("Code for HCF of two number:\n")
print()
num1=int(input("Enter first number :\n"))
num2=int(input('Enter second number :\n'))
minimum=min(num1,num2)
for loop in range (minimum,1,-1):
    if num1%loop==0 and num2% loop ==0:
        HCF=loop
        break
print(f"THE HCF OF {num1} and {num2} is {HCF} ")