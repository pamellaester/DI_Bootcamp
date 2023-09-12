from exercisesXP import Dog 
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__( name, age, weight)
        self.trained = trained
        
    def train(self):
        self.bark()
        self.trained = True
    
    def play(self, *dogs):
        print(f"{self.name}, {', '.join(dogs)} all play together")
    
    def do_a_trick(self):
      list_print = ["stands on his back legs", "shakes your hand", "plays dead", "does a barrel roll"]
      if self.trained == True:
          choice = random.choice(list_print)
          print(f"{self.name} {choice}")
          
dog_1 = Dog("fifi", 6, 3)
dog_2 = Dog("theo", 2, 7)
dog_3 = Dog("bella", 5, 11)
dog_2.train()
dog_2.do_a_trick()
