n=int(input("enter a number:"))
original=n
rev=0
while n>0:
    rev=(rev*10)+(n%10)
    n=n//10
if original==rev:
        print(rev,"is a palindrome")
else:
        print(rev,"is not palindrome")
