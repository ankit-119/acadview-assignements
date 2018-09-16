dict1={}
n=int(input("enter the no students "))
for i in range (0,n):
    x=input("enter name")
    dict1[x]={input("enter subject"):int(input("enter marks")) for j in range(2)}
    find=input("enter name to search")
for x,y in dict1.items():
    if(x==find):
        print("Match found")
        print("Marks of student ",y)
        break
    else:
        print("not found")
        
