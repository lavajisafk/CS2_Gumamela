import math

point_x1 = float(input("enter the x1:"))
point_x2 = float(input("enter the x2:"))
point_y1 = float(input("enter the y1:"))
point_y2 = float(input("enter the y2:"))

#distance = sqrt(pow(point_x2-point_x1, 2) + pow(point_y2-point_1, 2)

point_a = pow(point_x2 - point_x1, 2)
point_b = pow(point_y2 - point_y1, 2)
result = point_a + point_b
distance = math.sqrt(point_a + point_b)

print("the distance is", distance)

#area_of_circle = (math.pi * math.pow(radius, 2))
#print("\nThe area of circle", area_of_circle)
