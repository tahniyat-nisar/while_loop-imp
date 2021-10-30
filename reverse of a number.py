i=int(input("enter a number to get reversly printed:"))
reverse=0
while i>0:
    reverse=(reverse*10)+i%10
    i=i//10
print(reverse)
