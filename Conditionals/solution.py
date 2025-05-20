# 1. Age Group Categorization (Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).)

# methods to convert datatype

# age  = int(input("enter your age: "))

# age_in_int = int(age)

age = 20

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")


# 2. Movie Ticket Pricing -(Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.)

age = 26
day = "wednesday"

price = 12 if age >= 18 else 8

if day == "wednesday":
    price = price - 2
    # price -= 2

print("Ticket Price For You $", price)


# 3. Grade Calculator :Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = 185

if score >= 101:
    print("please verify your score")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)


# 4. Fruit Ripeness Checker : Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

BananaColor = "Yellow"

if BananaColor == "Green":
    print("Unripe")
elif BananaColor == "Yellow":
    print("Ripe")
elif BananaColor == "Brown":
    print("Overripe")



Fruit = "Apple"
Color = "Yellow"

if Fruit == "Apple":
    if Color == "Green":
        print("Unripe")
    elif Color == "Yellow":
        print("Ripe")
    elif Color == "Brown":
        print("OverRipe")



# 5. Weather Activity Suggestion Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

whather = "snowy"

if whather == "sunny":
    print("go for a walk")
elif whather == "rainy":
    print("read a book")
elif whather == "snowy":
    print("build a snowman")

# 6. Transportation Mode Selection Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

Distance = 16

if Distance <= 3:
    print("walk")
elif Distance <= 15:
    print("get a bike")
else:
    print("get a car")


# 7. Coffee Customization Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

coffeeOrder = "Small"
ExtraShot = True

if ExtraShot:
    coffee = coffeeOrder + " coffee with an extra shot"
else:
    coffee = coffeeOrder + " coffee"

print("order: ", coffee)


# 8. Password Strength Checker Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = 8

if password <= 6:
    print("your password is week")
elif password <=10:
    print("your password strength is medium")
else:
    print("strong password")

# or

password = "abc@1234"
password_length = len(password)

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is: ", strength)


# 9. Leap Year Checker Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = 2028

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print( year, " is a leap year")
else:
    print( year, " is not a leap year")


# 10. Pet Food Recommendation Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

age  = 5
typeofPet = "cat"

if typeofPet == "dog":
    if age <= 2:
        print("puppy food")
    else:
        print("senior dog food")

if typeofPet == "cat":
    if age >= 5:
        print("senior cat food")
    else:
        print("junior cat food")