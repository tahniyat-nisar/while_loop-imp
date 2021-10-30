n=int(input("enter a number:"))
if n>0:
    x=str(n)
    y=len(x)
    count=0
    sum=0
    while count<=y:
        r=((n%10))*(2**count)
        sum=sum+r
        n=n//10
        count=count+1
    print(sum)
                                                                                                                                                                                                            