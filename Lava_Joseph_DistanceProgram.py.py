import math

#Ask the user to enter the coordinates of the first point and second point
point_x1 = float(input("enter the x1:"))
point_x2 = float(input("enter the x2:"))
point_y1 = float(input("enter the y1:"))
point_y2 = float(input("enter the y2:"))

#Compute the distance using the distance formula
point_a = pow(point_x2 - point_x1, 2)
point_b = pow(point_y2 - point_y1, 2)
result = point_a + point_b
distance = math.sqrt(point_a + point_b)

#Display the results
print("the distance is", distance)


