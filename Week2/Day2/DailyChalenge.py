# exercise 1:

sequence = []
user_insert = int(input("Insert a number:"))
user_length = int(input("Inser a number"))
for i in range(1 ,user_length + 1):
    sequence.append(user_insert * i)
    print(sequence)


# exercise 2:

user_question = input("Insert a word with duplicated letters. Exemplo= looooolllaaaa")

result = "".join(dict.fromkeys(user_question))
print(result)

word = "ttiiiiittlllee"
new_word = "t"
word
