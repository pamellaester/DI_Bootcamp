# #exercise 1: Pets
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
  
# cat_1 = Bengal("lulu", 4)  
# cat_2 = Chartreux("gabi", 2) 
# cat_3 = Siamese("steff", 6) 
# all_cats = [cat_1, cat_2, cat_3]
# sara_pets = Pets(all_cats)
# sara_pets.walk()


# #exercise 2: Dogs
class Dog:
    
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        print(f"{self.name} is barking")
    
    def run_speed(self):
        self.speed = (self.weight/self.age*10)
        return self.speed

    def fight(self, other_dog):
        self.another = other_dog
        if self.another.speed > self.name.speed:
            print(f"{self.another} is the winner")
        else:
            return (f"{self.name} is the winner")
    
dog_1 = Dog("fifi", 6, 3)
dog_1.bark()
dog_2 = Dog("theo", 2, 7)
dog_2.bark()
dog_3 = Dog("bella", 5, 11)
dog_3.bark()

dog_1.fight(dog_3)

# Exercise 3 : Dogs Domesticated

