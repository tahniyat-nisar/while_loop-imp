n=int(input("enter a number:"))
i=1
sum=0
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if sum==n:
        print("it is perfect number")
else:
        print("it is not perfect number")
