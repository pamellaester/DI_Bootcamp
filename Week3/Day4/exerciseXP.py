# Exercise 1 – Random Sentence Generator

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

