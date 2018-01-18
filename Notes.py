"""print("Hello world")

# Sergio Yanez


a = 4
b = 3

print(3 + 5)
print(5 - 3)
print(3 * 5)
print(3 ** 5)
print(6 / 2)

print()
print("Try to figure this how this works")
print(13 & 12)

# the "%" sign is a modulus it finds the remainder

car_name = "Wiebe Mobile"
car_type = "BMW"
car_cylinders = 8
car_mpg = 5000.9

print("I have a car called %s. It's pretty nice." % car_name)
print("I have a car called &s. It's a %."(car_name, car_type))  # watch the order

# Here is where we get a little fancy
print("what is your name?")
name = input(">_")
print("hello %s." % name)
"""
age = input("How old are you?")
print("%s?! That's really old. You belong in a retirement home." % age)


# Functions


def print_hw():
    print("Hello world.")
    print("Enjoy the day.")


print_hw()


def say_hi(name):  # Name is a "parameter"
    print("Hello %s" % name)
    print("Coding is great!")


say_hi("John")


def print_age(name, age):
    print("%s is %d years old" % (name, age))
    age = age + 1
    print("Next year, %s will be %d years old" % (name, age))


print_age("John", 15)


def algebra_hw(x):
    return x**3 + 4*x**2 + 7 * x - 4

print(algebra_hw(3))
print(algebra_hw(4))
print(algebra_hw(5))
print(algebra_hw(6))
print(algebra_hw(7))



# if statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80: # elif
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

print(grade_calc)

# Lists
the_count = [1, 2, 3, 4, 5]
cheeseburger_ingredients = ['cheese', "beef", "sauce", "sesame seed bun", " avocado", "onion"]
print(cheeseburger_ingredients[3])
print(len(cheeseburger_ingredients))

# Going through lists
for generic_item_name in cheeseburger_ingredients:
    print(generic_item_name)

length = len(cheeseburger_ingredients)
range(5) # A list of numbers 0 through 4
range(len(cheeseburger_ingredients)) # Generate a list of all indices

for num in range(lrn(cheeseburger_ingredients)):
    item = cheeseburger_ingredients[num]
    print("The item at index %d is %s" % (num, item))




