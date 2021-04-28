def akpobome(x1, x2, y2, y1):
    # Algorith to calculate the distance between two points
    distance = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5 # option 1
    # distance2 = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)) # option 2
    # distance3 = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1),2)) # option 3
    return distance

x1 = int(input("Enter the value for x1: "))
x2 = int(input("Enter the value for x2: "))
y1 = int(input("Enter the value for y1: "))
y2 = int(input("Enter the value for y2: "))

result = akpobome(x1, x2, y1, y2)

print("distance between", (x1, x2), "and", (y1, y2), "is: ", result)
