import json
import enchant

class AnagramChecker:
    def __init__(self,text_file):
        with open ("sowpods.txt", "r") as text_file:
         self.word_list = text_file

    def is_valid_word(word):
        user_input = input("insert a word: \n")
        user_input = enchant.Dict("en_US")
        if user_input == True:
            return(f"{user_input} is a valid word!")
        else:
            return(f"{user_input} is a not valid word!")
    
        

    def get_anagrams(word):
        pass
        

   
    # def is_anagram(word1, word2):
    #     pass