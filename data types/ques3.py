lst1=[]
n=int(input("enter no of elements"))
for i in range (0,n):
    x=input("enter elements")
    
    lst1.append(x)
find=input("enter no to search")
p=lst1.count(find)
print(p)
