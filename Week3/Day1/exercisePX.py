# Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    def show_info(self):
        print(f"The dog name is {self.name} and his name is {self.age}")

first_cat = Cat("chica",3)
second_cat = Cat("lola",6)
third_cat = Cat("suzy",9)



show_info(first_cat)
show_info(second_cat)
show_info(third_cat)

def longest_age(self):
  for cat_age in Cat:
    if longest_age == max(self.values()):
     print(f"The oldest cat is {cat_name}, and is {cat_age }years old.")

# Exercise 2 : Dogs

class Dog:
   
   def __init__(self, name, height):
    self.name = name
    self.height = height

   def bark(self):
    print(f"{self.name} goes woof!")

   def jump (self):
    print(f"{self.name} jumps {self.height} cm high!”. {self.height} =={self.height}"*2)

   def info(self):
     print(f"the dog name is :{self.name} and the height is: {self.height} cm. ")

davids_dog = Dog ("Rex",50)

davids_dog.info()
davids_dog.bark()
davids_dog.jump()

# Exercise 3 : Who’s The Song Producer?

class song:
  def __init__(self,lyrics):
    self.lyrics = lyrics
  
  def sing_me_a_song(self):
    for elem in self.lyrics:
      print(elem)

  
  
  
  
  
  
stairway = song(["Theres a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])
    
stairway.sing_me_a_song()  


#exercise 4 : Afternoon At The Zoo

class zoo:
  def __init__(self,zoo_name):
    self.name = zoo_name
    self.animal = ()  

  def add_animal(self,new_animal,amount = 1):
    if new_animal in self.animal:
      self.animal[new_animal] += amount
    else:
      self.animal[new_animal] = amount

    
  def get_animals(self):
    for new_animals in self.animal:
     sentence = f"this is all animals in {self.name}: {self.animal}"
    return sentence
  
  def sell_animal(self,animal_sold,amount = 1):
    if animal_sold in self.animal:
     self.animal[animal_sold] -= amount
    else:
      self.animal[animal_sold] = amount

  def sort_animals(self):
    list_types = sorted(list(self.animal.keys()))
    return list_types

  def get_groups (self):
    if self.animal in list_type:
      print()


ramat_gan_safari = zoo()
  


