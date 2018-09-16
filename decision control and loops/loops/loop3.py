lst1=[]

sq=0
n=int(input("enter the number of element you want to enter"))
for i in range(1,n+1):
    x=int(input("enter the number"))
    lst1.append(i)

lst2=[]
for j in range(0,len(lst1)):
      
    p=lst1[j]
    sq=p*p
    lst2.append(sq)


print(lst2)
    
