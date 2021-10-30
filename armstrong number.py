n=int(input("enter a number:"))
sum=0
original=n
while n>0:
    x=str(original)
    y=len(x)
    z=int(n)
    r=(z%10)**y
    n=n//10
    sum=sum+r
print(sum)
if original==sum:
        print(sum, "= armstrong number")
else:
        print(sum,"is not a armstrong number")

