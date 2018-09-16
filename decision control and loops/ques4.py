age=int(input("enter the age"))
sex=input("Enter sex(M/F)")
status=input("Enter the status(Y/N)")
if(age<20 or age>60):
        print("ERROR")
elif(sex=='F' or sex=='f'):
    print("This person will work only in urban areas")
elif(age>=20 or age<=40):
        print("this person can work anywhere")
elif(sex=='M' and (age>=40 or age<=60)):
        print("This person will work in urban areas")
elif(age<20 or age>60):
        print("ERROR")
