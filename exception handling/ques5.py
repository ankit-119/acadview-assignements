#IMPORT ERROR
try:
    import date
except ImportError:
    print("import error")
    
 #VALUE ERROR   
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("Index error")
    
 #VALUE ERROR   
try:
    n=input("enter integer")
    n=int(n)
except ValueError:
    print("Value error")
else:    
    print("value is inserted")



        
        
    
