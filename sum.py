# write a python program to calculate the sum of 3 given nos.if the values are equal,return 3 times their sum

x=int(input("enter the first no:"))
y=int(input("enter the second no:"))
z=int(input("enter the third no:"))

def sum(x,y,z):
    if(x==y==z):
        sum=(x+y+z)*3
        print(sum)
    else:
        sum=x+y+z
        print(sum)
sum(x,y,z)







