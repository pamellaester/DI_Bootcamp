# Challenge 1

# ask_user = 

user_answer = input("insert a word \n")

word_dict = {}
for position,letter in enumerate(user_answer):
    if letter in word_dict:
        word_dict[letter].append(position)
    else:
      word_dict[letter] = [position]

print(word_dict)




# challenge 2


