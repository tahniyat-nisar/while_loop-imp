n=int(input("enter a number:"))
i=2
sum=0
count=1
while n>=count:
    if i%2==0:
        sum=sum+i
        i=i+2
        count=count+1
print(sum)

