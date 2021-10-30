n=int(input("enter a number:"))
i=1
count=0
while i<=n:
    if (n%i)==0:
        count=count+1
        # print(count) 
    i=i+1
print(count)