#Exception is ZeroDivisionError
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("no can't be divided by zero")
