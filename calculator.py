try:
    class calculator:
        def __init__(self,x,y):
            self.x=x
            self.y=y
        def addition(self):
            c=self.x+self.y
            return c
        def substraction(self):
            a=self.x-self.y
            return a
        def multiplication(self):
            b=self.x*self.y
            return b
        def division(self):
            div=self.x/self.y
            return div
        def floordiv(self):
            fd=self.x//self.y
            return fd
    class factorial:
        def __init__(self,n):
            self.n=n
        def fact(self):
            if self.n == 1:
               return self.n
            else:
                temp=self.n
                self.n-=1
                return temp*self.fact()
    try:
        print("---------------------------WELCOME-----------------------------------")
        choice=9
        while(choice!=0):
            print("1.addition")
            print("2.substraction")
            print("3.multiplication")
            print("4.division")
            print("5.Floor Division")
            print("6.Factorial")
            print("0 to exit")
            try:
                choice=int(input("enter the choice"))
                if(choice>7 and choice<0):
                    raise ValueError
            except:
                print("not valid choice")
            try:
                if(choice==1):
                    print("-----------FOR ADDITION-----------")
                    num1=int(input("enter the 1st no "))
                    num2=int(input("enter the 2nd no "))
                    calc=calculator(num1,num2)
                    print("the answer is",calc.addition())
                if(choice==2):
                    print("-----------FOR SUBSTRACTION------------------")
                    num1=int(input("enter the 1st no "))
                    num2=int(input("enter the 2nd no "))
                    calc=calculator(num1,num2)
                    print("the answer is",calc.substraction())
                if(choice==3):
                    print("-------------------FOR MULTIPLICATION------------------")
                    num1=int(input("enter the 1st no"))
                    num2=int(input("enter the 2nd no "))
                    calc=calculator(num1,num2)
                    print("the answer is ",calc.multiplication())
                if(choice==4):
                    print("---------------FOR DIVISION-----------------------")
                    num1=int(input("enter the 1st no "))
                    num2=int(input("enter the 2nd no "))
                    calc=calculator(num1,num2)
                    print("the answer is ",calc.division())
                if(choice==5):
                    print("--------------FOR FLOOR DIVISION---------------------")
                    num1=int(input("enter the 1st no"))
                    num2=int(input("enter the 2nd no"))
                    calc=calculator(num1,num2)
                    print("the answer is",calc.floordiv())
                if(choice==6):
                    print("--------------------FOR FACTORIAL--------------")
                    num1=int(input("enter the  no "))
                    cal=factorial(num1)
                    print("the answer is",cal.fact())
            except ZeroDivisionError:
                print("denominator can`t be zero")
            except ValueError:
                print("value error")
    except KeyboardInterrupt:
        print("program is terminated unexpectedly")
    else:
        print("program terminated as expected")
except:
    print("error in program
          ")
