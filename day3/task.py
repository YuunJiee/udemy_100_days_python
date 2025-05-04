print("Welcome to the rollercoaster!")
height = int(input("Waht is your height in cm? "))
pay = 0

if height > 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        pay += 5
    elif age <= 18:
        pay += 7
    elif age <= 55 and age >= 45:
        pay += 0
    else:
        pay += 12
    
    want_photo = input("Do you want to have a photo take? Type y for yes and n for No.")

    if want_photo == 'y':
        pay += 3
    
    print(f"Please pay ${pay}.")
else:
    print("Sorry you have to grow taller before you can ride.")
