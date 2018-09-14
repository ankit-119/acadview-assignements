def perfect(n):
    num=n
    sum=0
    for i in range(1,n):
        if (n%i==0):
            sum=sum+i
        if(sum==n):
            return n
        

#p=perfect(24)
#print(p)
for j in range(1,1001):
    
    print(perfect(j))
        
