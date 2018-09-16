lst1=[]
n=int(input("enter no of element you want to enter"))
for i in range(0,n):
    num=int(input("enter the elements of list"))
    lst1.append(num)
print(lst1)
find=int(input("enter the no you want to search"))
for i in range(0,n):
    if(lst1[i]==find):
        lst1.remove(lst1[i])
        break
    
print(lst1)
    
    
