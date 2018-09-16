quantity=int(input("Enter the quantity"))
cost=quantity*100
if(cost>1000):
    cost=cost-(0.1*cost)
    print("cost of item is= ",cost)
else:
    print("Cost of item is =",cost)
