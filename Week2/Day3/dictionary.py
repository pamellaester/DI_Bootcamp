# price = {
#     "apple" : 2,
#     "banana" : 5,
#     "mango" : 10,
# }

# user_word = input("wich fruit do you want? \n")


# print(price[user_word])

# # exercise

# # create a new list that only contains the uppercased words
# # words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']

# words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
# new_list = [ x for x in words if x.isupper()]
# print(new_list)

playlist = {
    'title': "Hello World",
    'author': "Planet",
    'songs': [
        {
            'song_title': "Song One",
            'artist': ['Artist 1', 'Artist 2'],
            'duration': 4.31,
        },
        {
            'song_title': "Song Two",
            'artist': ['Artist 1'],
            'duration': 2.53,
        },
        {
            'song_title': "Song Three",
            'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
            'duration': 3.43,
        }
    ]
}

total_duration = 0
for music in playlist['songs']:
    total_duration += music ['duration']
print(f"the total duration is {total_duration}")



