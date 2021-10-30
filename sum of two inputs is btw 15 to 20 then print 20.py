# i=int(input("enter a number:"))
# j=int(input("enter a number"))
# if i>0 and j>0:
#     sum=i+j
# while sum%5==0:
#     print(sum)
#     if sum%5!=0:
#          x=sum%5
#          y=i+j
#          z=(i+j)+x
#          print(z)
#     print(sum)
# else:
#     if sum%5!=0:
#         x=sum%5
#         y=sum+x
#         if y%5==0:
#             print(y)



i=int(input("enter a number:"))
j=int(input("enter a number:"))
if i>0 and j>0:
    sum=i+j
    if sum%5==0:
        print(sum)
    elif sum%5!=0:
        x=sum%5
        add=0
        while add<=5-x:
            # print(sum+add)
            add=add+1
        print(sum+add-1)
            
        
        
        # add=0
        # while add<=5:
        #     add=add+sum
        #     add
        #  print(x)
        # t=5-x
        # print(t)
        # s=str(t)
        # t=0
        # while t<=len(s):
        #     t=t+1
        # print(t+sum)




# add=0
# while add<=5:
#         add=add+1
#         temp=
#         print(sum+add)

