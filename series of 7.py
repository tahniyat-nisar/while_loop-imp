n=int(input("enter any number to get series in 7:"))
while n>=7:
    i=n%7
    a=n-i
    if a%7==0:
        print(a)
    n=n-7
