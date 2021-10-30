n=int(input("enter a number to find sum of cubes of its digits:"))
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
    print(sum)