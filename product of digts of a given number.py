n=int(input("enter a number to find product of its digits"))
product=1
while n>0:
    product=product*(n%10)
    n=n//10
    print(product)