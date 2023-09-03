#Exercise 1 : Hello World-I Love Python
print("hello world \n"*4,"I love u python\n"*4)

#Exercise 2 : What Is The Season ?

months_question = input("Insert a month(1-12): \n")
if 3 <= int(months_question) <= 5:
    print(f"The weather on {months_question} is Spring")
elif 6 <= int(months_question) <= 8:
    print(f"The weather on {months_question} is Summer")
elif 9 <= int(months_question) <= 11:
    print(f"The weather on {months_question} is Autumm")
elif int(months_question) == 12:
    print(f"The weather on {months_question} is Winter")
elif int(months_question) <= 2:
    print(f"The weather on {months_question} is Winter")
else:
    print(f"error!Try Again!")



