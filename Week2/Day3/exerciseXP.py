# Exercise 1 : Convert Lists Into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

ages = zip(keys,values)

print(dict(ages))

# # Exercise 2 : Cinemax
ticket_prices = {
    "free" : 3,
    "10_ticket" : 10,
}

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
age = family.values()

family_price = age 
for family.values in family:
 if age < "free":
        print("  You get in free!")
 elif age < 13:
        print("  Your ticket is $10.")
 else:
        print("  Your ticket is $15.")
print(family_price)
       
    


# Exercise 3: Zara

brand = {
    "name": 'Zara',
    "creation_date" : 1975,
    "creator_name" : 'Amancio Ortega Gaona',
    "type_of_clothes" : [ 'men', 'women', 'children', 'home' ],
    "international_competitors" : [ 'Gap', 'H&M', 'Benetton' ],
    "number_stores" : 7000, 
    "major_color" : {
        "France": 'blue', 
        "Spain": 'red', 
        "US": [ 'pink', 'green']
    }
}
      
brand['number_stores'] = 2
print(brand)

brand["country_creation"] = 'Spain'

srch = brand.get("international_competitors")
print(srch)

brand["international_competitors"].append(" Desigual")
print(brand)

del brand['creator_name']
print(brand)

print(brand['international_competitors'][-1])


print(brand["major_color"]["US"])  

amount = range(len(brand))   
print(amount)

print(brand.keys())

more_on_zara = {
    "creation_date": '1975', 
    "number_stores": '10000', 
}

brand.update(more_on_zara = {
    "creation_date": '1975', 
    "number_stores": '10000',} )
print(brand)

print(more_on_zara['number_stores'])


# Exercise 4 : Disney Characters

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# /1
# word_dict = {}
# for position, letter in enumerate(users):
#     word_dict[letter] = position
# print(word_dict)

# /2
# print(dict(enumerate(users)))

#  /3
# users.sort(key=str.lower)
# word_dict = {}
# for position, letter in enumerate(users):
#     word_dict[letter] = position
# print(word_dict)

# /4
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
for index,value in enumerate(fruits):
    fruits[index] += "s"

disney_users_a = {name: index for index, name in enumerate(users)}
print(disney_users_a)

disney_users_b = {index: name for index, name in enumerate(users)}
print(disney_users_b)

new_list = sorted(users)
disney_users_c = {name: index for index, name in enumerate(new_list)}
print(disney_users_c)

disney_users_d = {name: index for name, index in disney_users_a.items() 
                  if 'i' in name
                  if name[0] in ('M', 'P')
                  }
print(disney_users_d)



# /Users/pamella/Desktop/DI_Bootcamp/Week2/Day3/exerciseXP.py
