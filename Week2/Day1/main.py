# print("hello world")
# #method used to display some value
# pet_animal = "cat"
# #assign a value to the variable
# #declaring a variable and assigning a value
# setence = "my favorite is a" + pet_animal  

# #integer
# year = 2023
# setence_two = str(year) + "is the current year"

# next_year = year + 1


# year = 2023
# age = 19
# city = "tel aviv"
# #string formatting
# setence_three = f"{year} is the currente year, I'm {age} year old and i live in {city}"
# print(setence_three)

# first_name = "Pamella Ester"
# last_name = "Sousa"

# setence_four = f"My full name is {first_name} {last_name}"
# print(setence_four)

# my_age = 21
# my_future_age = my_age + 123879
# sentence_five = f"my future age will be {my_future_age}"
# print(sentence_five)
# print("my full name is {} {}".format(first_name,last_name))

sentence = "10 miles"
question = input("how many miles do you want to convert?\n")
sentence = sentence.repalce("miles",question)
print(sentence)
        
user_miles =float(input("give me a number of miles"))    
convert_ti_km = user_miles *1.60934   