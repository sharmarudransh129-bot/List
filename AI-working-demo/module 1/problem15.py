print("Code for sum of the digitsin a given number:\n")
num=int(input("Enter the number :\n"))
temp=num
sum=0
while num>0:
    remainder= num%10
    sum=sum +remainder
    num=num//10
print(f"The sum of digits of {temp} is {sum}")