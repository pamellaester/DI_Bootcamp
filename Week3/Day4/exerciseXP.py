# Exercise 1 – Random Sentence Generator

import random
def get_word_from_file():
    with open("random_word.txt", "r") as random_file:
        content = random_file.read()
        collection_word = content.split()
    return collection_word

def get_random_sentence(lenght, some_list):
    list_sentence = random.sample(some_list, lenght)
    sentence = " ".join(list_sentence).lower()
    return sentence

def main():
    print("this program will take the user answer as a lenght for a sentence as i do below but if the number is not between 2-20 then i will raise an error and end the program if not i will call the function below")
    user_lenght = int(input("chose a lenght between 2-20 "))
    try:
        if 2 <= user_lenght <= 20:
            print(get_random_sentence(user_lenght, new_list))
    except ValueError:
        print("lenght is not between 2-20")
        

new_list = get_word_from_file()
print(get_random_sentence(5, new_list).capitalize())
main()


# Exercise 2: Working With JSON

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


first = json.loads(sampleJson)
first["company"]["employee"]["payable"]["salary"]
first["company"]["employee"]["birth_date"] = "08/01/2002"
print(first["company"]["employee"]["birth_date"])

with open("exerciseXP.json", "w") as file:
    json.dump(first, file)

