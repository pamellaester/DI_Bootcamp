string_question = input("insert a string \n")
if string_question > len(10):
    print("string not long enough")
elif string_question < len(10):
    print("string too long")
elif string_question == len(10):
    print("perfect string")