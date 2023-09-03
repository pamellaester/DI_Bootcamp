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



