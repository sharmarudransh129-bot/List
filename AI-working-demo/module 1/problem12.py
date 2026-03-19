print("CODE TO COUNT THE NUMBER OF DIGITS IN A GIVEN NUMBER:\n")
print()
num=int(input('ENTER THE  NUMBER :\n'))
count=0
temp=num
while num>0:
        count = count +1
        num=num//10
print(f"The number of digits in {temp} is {count}")