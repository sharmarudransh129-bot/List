#num1=int(input("Enter the first number :\n"))
#print('Code to print prime number in range :\n')
#num2=int(input("Enter the second number :\n"))
#minimum=min(num1,num2)
#maximum=max(num1,num2)
#print(f"The prime number between range {minimum} and {maximum}:")
#count=0
#for loop in range (minimum,maximum +1,1):
#    for prime in range (2, (loop//2)+1,1):
#        loop%prime==0
#        count+=1
#        break
#    if count ==0:
#        print(f"{loop}",end="")
print('Code to print prime numbers in range :\n')

num1 = int(input("Enter the first number :\n"))
num2 = int(input("Enter the second number :\n"))

minimum = min(num1, num2)
maximum = max(num1, num2)

print(f"The prime numbers between range {minimum} and {maximum} are:")

for loop in range(minimum, maximum + 1):

    if loop < 2:
        continue

    count = 0

    for prime in range(2, (loop//2) + 1):
        if loop % prime == 0:
            count += 1
            break

    if count == 0:
        print(loop, end=" ")