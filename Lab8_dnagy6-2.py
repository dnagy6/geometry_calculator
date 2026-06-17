"""
---------------------------------------------------------
Name: Dakota Nagy
Date: June 17, 2026
Assignment: Lab 8 - Geometry Calculator
Description: A menu-driven program that imports custom 
             modules to calculate the area and perimeter/
             circumference of circles and rectangles.
---------------------------------------------------------
"""

# We use aliases (as c, as r) because both modules contain a function named 'calc_area'. By using aliases, we can avoid naming conflicts and clearly indicate which module's function we are calling.
import circle as c
import rectangle as r

# We need to start a loop that runs until the user chooses to exit the program. Inside the loop, we will display a menu of options for the user to choose from. Based on the user's choice, we will call the appropriate functions from the circle and rectangle modules to perform the calculations.

user_choice = ""

while user_choice != "5":
    print("Geometry Calculator")
    print("1. Calculate the area of a circle")
    print("2. Calculate the circumference of a circle")
    print("3. Calculate the area of a rectangle")
    print("4. Calculate the perimeter of a rectangle")
    print("5. Exit")

    user_choice = input("Enter your choice (1-5): ")

    if user_choice == "1":
        radius = float(input("Enter the radius of the circle: "))
        area = c.calc_area(radius) # 'c' tells it to look in circle.py
        print(f"The area of the circle is: {area:.2f}")
    elif user_choice == "2":
        radius = float(input("Enter the radius of the circle: "))
        circumference = c.calc_circumference(radius) # 'c' tells it to look in circle.py
        print(f"The circumference of the circle is: {circumference:.2f}")
    elif user_choice == "3":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = r.calc_area(length, width) # 'r' tells it to look in rectangle.py
        print(f"The area of the rectangle is: {area:.2f}")
    elif user_choice == "4":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        perimeter = r.calc_perimeter(length, width)
        print(f"The perimeter of the rectangle is: {perimeter:.2f}")
    elif user_choice == "5":
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")