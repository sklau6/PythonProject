def name_printer(user_name):
    print(user_name)

name = input("Please enter your name.")
name_printer(name)

def hello_world_printer():
    print("hello world")

hello_world_printer()

# Variables holding the prices of the six items:

pasta = 16.68  # penne 16 oz, pack of 12
sauce = 6.98  # Arrabiata sauce 24oz
garlic = 16.78  # 20 pack garlic clove
seasoning = 15.26  # Italian Seasoning
bread = 3.00  # Baguette twin pack
meatballs = 4.39  # 12 oz bag of meatballs
# A subtotal is the sum of all prices before any sales taxes or discounts are added.

# round() was used to round the subtotal to 2 decimal places since the sum of any amount of numbers that all have 2
# numbers after the decimal will always have 2 numbers after its decimal point.
subtotal = round((pasta + sauce + garlic + seasoning + bread + meatballs), 2)
print(subtotal)

summed = 2 + 3
difference = 10 - 8
divided = 1000 / 10
product = 7 * 5
exponent = 3 ** 8
floored = 10 // 3
mod = 17 % 15  # could have used 3, 5, or 15 to get 2 as a result
int_num = 24601   # int_num is a variable which has been assigned an integer
print(int_num)    # prints the integer assigned to int_num
print(True)       # uses print() to display the Boolean value True
print(1 + 1 + 1)  # prints the result of the expression 1 + 1 + 1
print("Helloworld "+mod.__str__())

to_slice = "Just do it!"
print(to_slice[10])   # prints "!"
print(to_slice[5:7])  # prints "do"
print(to_slice[8:])   # prints "it!"
print(to_slice[:4])   # prints "Just"
print("Don't " + to_slice[5:])  # prints "Don't do it!"

float_num = 6.7                                     # variable that has been assigned a float
print(type(float_num))                              # prints the type of float_num
print(str(float_num) + " is a float.")              # prints "6.7 is a float."
print("\"Hello, I'm Aaron, it's nice to meet you!\"")  # prints "Hello, I'm Aaron, it's nice to meet you!"

print("*******\n *****\n  ***\n   *")

name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")

print("So your name is " + name + ", your quest is " + quest + ", and your favorite color is " + color + ".")

use_int = int(input("Please enter an integer."))

print(use_int + 10)







