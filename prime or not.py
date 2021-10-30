n=(int(input("enter a number know wheather it is prime or not:")))
i=1
count=0
while i<=n:
    if n%i==0:
        count=count+1
    i=i+1
if count==2:
    print(n,"is a prime number")
else:
    print(n,"is a composite number")
