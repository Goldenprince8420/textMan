from vocabulary import *
from translator import *
from analyser import *
from modifier import *

if __name__ == '__main__':
    print("Hello User!!")
    word = "help"
    dictionary = MeaningMaster()
    # dictionary.get_meaning(word)
    # dictionary.translate_the_word(word, lang = 'hi')
    translate = Translator()
    sentences = ["I am Rahul Golder", "I am in Kolkata"]
    print(sentences)
    # translate.show_all_lang_codes()
    translate.detect_lang(sentences)

