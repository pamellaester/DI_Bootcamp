# # Exercise 1: Currencies



# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __str__(self) :
#         return f"{self.amount} {self.currency}"

#     def __int__(self) :  
#         return self.amount

#     def __repr__(self) :
#         return f"{self.amount} {self.currency}"
    
#     def __add__(self,another_currency) :
#         if self.currency == another_currency.currency:
#          return self.amount + another_currency.amount
#         else:
#             return f"TypeError: Cannot add between Currency type {self.currency} and {another_currency.currency}"
    
    
    
        
    

# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# print(c1)
# print(int(c1))
# print(int(c1) + 5)
# print(int(c1 + c2))
# c1.amount += 5
# print(c1)
# c1.amount += c2.amount
# print(c1)
# print(c1 + c3)


# # Exercise 2: Import

# from func import __add__ 

# Exercise 3: Random Module
# import random

# class ramdom_number:

#     def __init__(self,number=random.randint(1,100)) :
#         self.number = number

#     def same_number(self,other_number):
#        if other_number == self:
#          return f"It's the same number! \n random number is: {self.number}"  
#        else:
#            return f"It's not the same number! Try again! \n random number is: {self}"


# number_question = input(f"insert a number: \n")   
# question = ramdom_number(number_question)
# print(question.same_number())

# Exercise 4: String Module
# import string
# import random

# N = 5


# res = ''.join(random.choices(string.ascii_letters, k=N))
# print(f"The generated random string : " + str(res))

#  Exercise 5 : Current Date

# import datetime

# def current_date():
#    current_date1 = datetime.date.today()
#    return current_date1

# print(current_date())

# Exercise 6 : Amount Of Time Left Until January 1st

# from datetime import datetime

# date1 = datetime.now()
# date2 = datetime(day=1, month=1, year=2024)

# timedelta = date2 - date1
# print(timedelta)

# Exercise 7 : Birthday And Minutes

# from datetime import date    
# age = date.today()-date(2002,1,8)
# print(age.days)

# # Exercise 8 : Faker Module

from faker import Faker
fake = Faker()



def add_dict(num_users):
    users_list = []
    for i in range(1,num_users):
        users = {}
        users["name"] = fake.name()
        users["adress"] = fake.adress()
        users["language_code"] = fake.random_element(elements = ("English","Spanish","Portuguese","Hebrew","French"))
        users_list.append(users)
    return users_list

print(add_dict())






















