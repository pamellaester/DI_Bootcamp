class Text:
    def __init__(self,text_to_analyse):
        self.text_to_analyse = text_to_analyse.lower().replace(".","")
        self.all_fequencies = self.get_frequencies()

    def get_frequencies(self):
        dict_word = {}
        list_words = self.text_to_analyse.split(" ")
        for word in list_words:
            dict_word = list.count(word)
        return dict_word

    def get_frequency_word(self,word):
        if word in self.all_fequencies:
            return self.all_fequencies[word]
        else:
            None
        
    def most_common_word(self):
        most_common_words = []
        values_dict = self.all_fequencies.values()
        max_value = max(values_dict)
        for word in self.all_fequencies:
            if self.all_fequencies[words] == max_value:
                most_common_words.append(word)
        return f"the most common words are {most_common_words}"


        


txt = Text("")
print(txt.all_fequencies)
print(txt.get_frequency_word("good"))

