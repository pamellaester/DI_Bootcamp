# Exercise 1 : What Are You Learning ?

# def display_message():
#     print("python class4,we are learning python!")

# display_message()

# Exercise 2: What’s Your Favorite Book ?

# def favorite_book(title):
#    return print('One of my favorite books is ' + title)

# favorite_book('Alice in Wonderland')


# Exercise 3 : Some Geography

# def describe_city(city,country ='usa'):
#     print(city + ' is in ' + country)

# describe_city('Reykjavik','Iceland')

# Exercise 4 : Random voltarrrrrrrrrrr

# def ramdom_number(num,nun):
#     if num == nun:
#         print('you got it right!')
#     elif num != nun:
#      return print("you've failed! your numbers was: " + num, nun)
    

# ramdom_number(5, 2)

# Exercise 5 : Let’s Create Some Personalized Shirts !

# def make_shirt(size,text):
#    print("The size of the shirt is " + size + " and the text is " + text )
   
# make_shirt('big','Hello world')


# Exercise 6 : Magicians …

# def show_magicians(a,b,c):
#     def make_great(d):
#       print(a,b,c)
#     print(show_magicians + make_great)
       

# show_magicians('Harry Houdini', 'David Blaine', 'Criss Angel')
# make_great("the Great")


# Exercise 7 : Temperature Advice

def get_random_temp(a):
 while(a > 100 or a < -10 ):
    print(int(input("")))

# get_random_temp(-10,40)
   

#  Exercise 8 : Star Wars Quiz

# questions = (
#     "What is Baby Yoda's real name?",
#     "Where did Obi-Wan take Luke after his birth?",
#     "What year did the first Star Wars movie come out?",
#     "Who built C-3PO?",
#     "Anakin Skywalker grew up to be who?",
#     "What species is Chewbacca?"
# )

# options = (
#     ("1. Grogu","2. Yoda"),
#     ("1. Takodana","2. Tatooine"),
#     ("1. 1797","2. 1977"),
#     ("1. Anakin Skywalker","2. Luke Skywalker"),
#     ("1. Jedi","2. Darth Vader"),
#     ("1. Wookiee","2. Kowakian monkey-lizard")
# )

# Answers = ("1","2","2","1","2","1")

# guesses = []

# score = 0 

# question_num = 0

# for question in questions:
#     print("---------------------------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)

    
#     guess = input ("enter (1,2): ")
#     guesses.append(guess)
#     if guess == Answers[question_num]:
#         score =+ 1 
#         print("CORRECT!")
#     else:
#         print("INCORRECT!")
#         print(f"{Answers[question_num]} is the correct answer")  
#     question_num += 1

# print("---------------------------------------")
# print(                "RESULT"                 )
# print("---------------------------------------")

# print("answers: ", end="")
# for answer in Answers:
#     print(answer,end="")
# print()

# print("guesses: ", end=" ")
# for guess in guesses:
#     print(guess,end=" ")
# print()

# score = int(score/len(questions)*100)
# print(f"Your score {score}%")