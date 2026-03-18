print("CODE TO REVERSE A NUMBER :\n")
print()
num=int(input('Enter the number :\n'))
temp=num
reverse=0
while num>0:
    remainder=num%10
    reverse=reverse*10+ remainder
    num=num//10
print(f'The  REVERSE OF {temp} IS {reverse}')
