file1=open("file.txt","r")
file2=open("file1.txt","w+")
n=file1.readlines()
file2.writelines(n)

file1.close()
file2.close()
file2=open("file1.txt","r")
print(file2.read())

