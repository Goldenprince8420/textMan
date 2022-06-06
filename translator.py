import googletrans


class Translator:
    def __init__(self):
        self.lang_codes = dict(map(reversed, googletrans.LANGUAGES.items()))
        self.translator = googletrans.Translator()

    def show_all_lang_codes(self):
        print(self.lang_codes)
        return

    def get_lang_code(self, lang):
        if lang not in self.lang_codes.keys():
            print("Your provided language is not  in the database!")
            return -1
        else:
            lang_code = self.lang_codes[lang.to_lower()]
        return lang_code

    def detect_lang(self, sentences, do_print = True):
        detects = self.translator.detect(sentences)
        if do_print:
            for detect, sentence in zip(detects, sentences):
                print(sentence)
                print(detect)
                # print("System Detects the sentence: \nSentence Language: {}\nConfidence: {}".format(detect.lang, detect.confidence))
        return detects

    def translate_to_lang(self, sentence, to_lang):
        translated_text = self.translator.translate(
            sentence,
            dest = self.get_lang_code(lang = to_lang)
        ).text
        print("The Sentence {} translated to the language {} is: {}".format(
            sentence, to_lang, translated_text))
        return translated_text



