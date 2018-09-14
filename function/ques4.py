def power(n,m):
    if(m!=0):
        return (n*power(n,m-1))
    else:
        return 1
x=int(input("enter the base"))
y=int(input("enter the power"))
p=power(x,y)
print(p)
    
    
