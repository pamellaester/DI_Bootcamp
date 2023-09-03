# exercise 1:
print("Hello world! \nHello world! \nHello world! \nHello world!")

# exercise 2:
print((99^3)*8)

# exercise 3:
# >>> 5 < 3 = (false)
# >>> 3 == 3 (true)
# >>> 3 == "3" = (false)
# >>> "3" > 3 = (false)
# >>> "Hello" == "hello" = (true)

# exercise 4:
computer_brand = "apple"
print(f"I have a {computer_brand} computer")

# exercise 5:
name = "Pamella Ester"
age = 21
shoe_size = 37
info = f"My name is {name}, I'm {age}, my shoe's size is {shoe_size}."
print(info)

# exercise 6:
a = 13
b = 7
if a >= b:
    print(f"hello world")
else:
    print(f"not hello world")

# exercise 7:
user_question = int(input("write a number"))
if (user_question % 2) == 0:
    print("{0} is Even".format(user_question))
else:
    print("{0} is Odd".format(user_question))

# exercise 8:
my_name = "pamella"
name_question = input("What's your name? \n")
if name_question == my_name:
    print("wow!! The progammer has the same name, what a coincidence!")
else:
    print("beautiful name you have!")

#exercise 9:

height_question = float(input("what is your height (inch)? \n"))
convert_to_cm = height_question*2.54
if convert_to_cm >=145:
    print("You are tall enough to ride.")
elif convert_to_cm < 145:
    print("You need to grow some more to ride.")  

print("out")  