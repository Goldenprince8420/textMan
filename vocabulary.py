from PyDictionary import PyDictionary


class MeaningMaster:
    def __init__(self):
        self.object = PyDictionary()

    def get_meaning(self, word, parts_of_speech = "Noun"):
        meaning = self.object.meaning(word)
        if parts_of_speech not in meaning.keys():
            if parts_of_speech != "Noun":
                print("The word is not applicable as the provided parts of speech!")
            parts_of_speech = meaning.dict.keys()[0]
        text = meaning[parts_of_speech]
        print("The word {} can be implied to these meanings:\n".format(word))
        for i in range(len(text)):
            print("{}: {}".format(i+1, text[i]))
        return

    def translate_the_word(self, word, lang):
        trans_word = self.object.translate(word, language = lang)
        print("The word {} in the provided language is: {}".format(word, trans_word))
        return


