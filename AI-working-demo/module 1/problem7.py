print('Code for Palindrome')
num=int(input('Enter the number:'))
rev=0
temp=num
while num>0:
    digit=num%10
    rev = (rev*10) + digit
    num=num//10
if rev ==  temp:
    print(f"the given number {temp} is palindrome")
else:
    print(f'the given number {temp} is not palindrome')