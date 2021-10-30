# n=int(input("enter a number to find its sum of even place digits and product of odd place digits:"))
n=int(input("enter a number"))
sum=0
product=1
while n>0:
    t=n%10
    if t%2==0:
        sum=sum+t
        print(sum)
        n=n//10
    elif t%2!=0:
        product=product*t
        print(product)
        n=n//10

