print("THE SUM OF FIRST N NUMBER :\n")
print()
num=int(input('Enter the number :\n'))
sum=0
for count in range (1,num+1,1):
    sum=sum+count

print(f"The Sum of first {num} number are {sum}")
