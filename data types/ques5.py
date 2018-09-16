lst1=[]
n=int(input("enter no of elements"))
for i in range (0,n):
    x=int(input("enter elements"))
    lst1.append(x)


lst2=[]
lst3=[]
m=int(input("enter no of elements"))
for i in range (0,m):
    y=int(input("enter elements"))
    lst2.append(y)

lst3=lst1+lst2
lst3.sort()
print(lst3)
