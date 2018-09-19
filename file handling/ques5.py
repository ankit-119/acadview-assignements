import random
file1=open('file4.txt','w')
for i in range(1,11):
    file1.writelines(str(random.randrange(1,100))+'\n')
file1.close()
file1=open('file4.txt','r')
file_content=file1.readlines()
file1.close()
file1=open('file4.txt','w')
sorting=[]
for i in file_content:
    sorting.append(int(i.strip()))
sorting.sort()
sorting=[str(i) for i in sorting]
file1.writelines('\n'.join(sorting))
file1.close()
