add comments in the play function

class Dog :

    def __init__(self, dog_name, dog_age, dog_color = "black", dog_energy = 100) :
        self.name = dog_name
        self.age = dog_age
        self.color = dog_color
        self.energy = dog_energy

    # method happybirthday increment the age by one
    def happy_birthday(self) :
        self.age += 1

    def show_info (self) :
        print(f"The dog name is {self.name}, his age is {self.age}, he is of color {self.color}")

    def go_to_groomer(self, owner_color) :
        self.color = owner_color

    def play (self, activity) :
    # this function create an action to play with:
    #if the dog does'nt enough to play it goes directly to the function :sleep
        if self.energy >= 10:
    #to play with a ball
            if self.energy >= 10 and activity == "ball" :
                self.energy -= 10
                print(f"{self.name} is playing ball - he has {self.energy} energy left")
    #to play with a frisbee
            elif self.energy >= 30 and activity == "frisbee":
                self.energy -= 30
                print(f"{self.name} is playing frisbee - he has {self.energy} energy left")
    #to play date (with another dog)
            elif self.energy >= 70 and activity.energy >= 70 and isinstance(activity, Dog) :
                self.energy -= 70 #lea_dog energy
                activity.energy -= 70 #activity is dan_dog
                print(f"{self.name} and {activity.name} are playing together - {self.name} has {self.energy} energy left - - {activity.name} has {activity.energy} energy left")
    #if the dog doesn't have energy left he goes to sleep
            else :
                print(f"You have {self.energy} left - You don't have enough energy to play {activity} \n")
                self.play(input("Please choose another activity between ball, frisbee and play date \n"))
        else :
            self.sleep()
    
    def sleep (self) :
    #this function makes the dog go to sleep and fullfuil the energy
        self.energy = 100
        print(f"{self.name} slept, he has {self.energy} energy")

lea_dog = Dog("Spock", 2)
dan_dog = Dog("Rex", 4, "white")
lea_dog.play(dan_dog)

# exercise

# Exercise 1 : Basic Classes
# Create a Employee class, With the attributes : firstname, lastname, age, job, salary

class Employee: 
    def __init__(self,firstname,lastname, age, job, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary

    def fullname(self):
        return f"this employee full name is {self.firstname} {self.lastname}"
    
    def happy_birthday(self):
        self.age += 1
        return self.age
    
    def get_promotion(self, promotion_amount):
        self.salary += promotion_amount


    def show_full_info(self) :
        print(f"this employee full name is {self.fullname()}, age : {self.age}, current job {self.job}, current salary: {self.salary} shekels")


user1 = Employee("Lea","Smith", 30, "developer" , 25000 )
user2 = Employee("David", "Schartz ", 20, "project manager", 20000 )

user1.show_full_info()
user2.show_full_info()



# 1. Create 2 users object and display their attribute
# - Lea Smith 30 years old developer 25000 shekels
# - David Schartz 20 years old project manager 20000 shekels
# Add those methods to the class
# get_fullname(self) : that return the firstname + lastname
# happy_birthday(self) : that return the age incremented by one
# get_promotion(self, promotion_amount) : that increment the salary of the user by the promotion
# show_info(self) : that will print the information of the employee --> name, age, job, salary
# Call all the methods

