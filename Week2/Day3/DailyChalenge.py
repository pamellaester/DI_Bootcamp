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

items_purchase = {
  "xilophone": "$40",
  "Honey": "$300",
  "Fan": "$140",
  "Bananas": "$400",
  "zPan": "$10",
  "Spoon": "$20"
}
wallet = "$100" 
convert_wallet = int(wallet.replace("$",""))
items_list = []
for item, price in items_purchase.items():
    convert_value = int(price.replace("$", ""))
    if convert_value < convert_wallet:
        convert_wallet -= convert_value
        items_list.append(item)
if len(items_list) == 0:
    print("nothing")
else:
    items_list.sort()
    print(items_list)


