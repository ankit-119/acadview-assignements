file1=open("file.txt","r")
file2=open("file1.txt","r")
a=file1.readlines()
b=file2.readlines()
file1.close()
file2.close()
x=list(zip(a,b))
print(x)
file3=open("file3.txt","w")
for i in x:
    for j in i:
        file3.write(j)
file3.close()

