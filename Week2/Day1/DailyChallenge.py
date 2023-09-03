import random


string_question = input("insert a string \n")
if len(string_question) < 10:
    print("string not long enough \n")
elif len(string_question) > 10:
    print("string too long \n")
elif len(string_question) == 10:
    print("perfect string \n")

first_character = string_question [0]
print(first_character)
last_character = string_question [-1]
print(last_character)

character = "helloworld"
for index in range(len(character)):
    print(character[:index+1])


# Original list
letter_list = ["H","e","l","l","o","w","o","r","l","d"]
print(letter_list)

# List after first shuffle
random.shuffle(letter_list)
print(letter_list) 

# List after second shuffle
random.shuffle(letter_list)
print(letter_list)


