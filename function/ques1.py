def calculatearea(r):
    r1=r
    area=3.1415*r1*r1
    return area
radius=float(input("enter the radius of sphere"))
area=calculatearea(radius)
print("Area of sphere is "+" "+str(area))
