#Exception is IndexError
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("list is out of index")
