n=int(input("guess the number stored inside:"))
while n>0:
    if n<=9 and n>=1:
        print("congrats,your guess",n,"is right")
        break
    else:
        print("sorry your guess is wrong")
        break