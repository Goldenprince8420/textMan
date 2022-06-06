from translator import Translator
from auto_corrector import correct
import gramformer
import styleformer
from cleantext import clean


class Modifier(Translator):
    def __init__(self):
        super(Modifier, self).__init__()
        self.corrector = None
        self.gf = None
        self.sf = None
        self.cleaner = clean

    def set_corrector(self, use_gpu = False):
        self.gf = gramformer.Gramformer(models = 1, use_gpu = use_gpu)
        return

    def set_styler(self, style_index):
        self.sf = styleformer.Styleformer(style = style_index)
        return

    def clean_text(self, text):
        cleaned_text = self.cleaner(text)
        return cleaned_text

    def correct_spelling(self, text):
        self.corrector = correct
        correct_spelled_sentence = self.corrector(text)
        print("The corrected sentence is: {}".format(correct_spelled_sentence))
        return correct_spelled_sentence

# Gramformer Models:
    # models = 1: Corrector(Currently Working)
    # models = 2: Detector(Not been Implemented yet)

    def correct_sentence(self, text):
        self.set_corrector()
        corrected_sentence = self.gf.correct(text)
        return corrected_sentence

# Styleformer Styles:
    # style = 0: Casual to Formal
    # style = 1: Formal to Casual
    # style = 2: Active to Passive
    # style = 3: Passive to Active

    def make_casual(self, text):
        style_index = 1
        self.set_styler(style_index = style_index)
        styled_sentence = self.sf.transfer(text)
        return styled_sentence

    def make_formal(self, text):
        style_index = 0
        self.set_styler(style_index)
        styled_sentence = self.sf.transfer(text)
        return styled_sentence

    def make_passive(self, text):
        style_index = 2
        self.set_styler(style_index)
        styled_sentence = self.sf.transfer(text)
        return styled_sentence

    def make_active(self, text):
        style_index = 3
        self.set_styler(style_index)
        styled_sentence = self.sf.transfer(text)
        return styled_sentence





