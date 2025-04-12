# Area = PI*r^2
CONSTANT = 2
PI = 22/7

# print("Enter the radius of the circle")
while True:
    try:
        user_input = input("Enter radius (CTRL + C to stop program) -> ")
        radius = float(user_input)

        if radius == 0:
            print("Radius cannot be zero and must be greater than 0")
        else:    
            area = PI * (radius ** CONSTANT)
            print("Area of circle with radius ", radius, " = ", area)
    except KeyboardInterrupt:
        print("Turning device off")
        break

