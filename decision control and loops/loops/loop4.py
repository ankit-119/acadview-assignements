list1=[21,'hello',12.344,'bye',12,44,34.55]
stringList=[]
floatList=[]
intList=[]
for i in list1:
    if(type(i)==float):
        floatList.append(i)
    elif(type(i)==int):
        intList.append(i)
    elif(type(i)==str):
        stringList.append(i)
print(stringList)
print(floatList)
print(intList)
