lst1=[]
e=0
o=0
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
for i in range(0,len(lst3)):
    if(lst3[i]%2==0):
        e=e+1
    else:
        o=o+1
print("number of even number are",e)
print("number of odd number aare",o)
        
