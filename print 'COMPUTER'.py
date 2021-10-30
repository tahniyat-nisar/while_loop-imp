k=int(input("enter no. of letters required to print your word:"))
sum=""
count=1
while count<=k:
    n=input("enter a alphabet:")
    if (n>="a" and n<="z")or(n>="A"and n<="Z"):
        count=count+1
        sum=sum+n
print(sum)
    

