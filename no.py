# write a python program to check entered no is btwn 100-700 or 700-900


no=int(input("enter the no:"))
for i in range(100,701):
    if(i==no):
        print(no,"in between 100-700")
for i in range(700,901):
    if(i==no):
        print(no,"in between 700-900")
