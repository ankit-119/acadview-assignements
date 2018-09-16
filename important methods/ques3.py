str1=input("Enter list seperated by commas")
str1=str1.split(',')
list1=[]
for i in str1:
    list1.append(int(i))
print(list1)
