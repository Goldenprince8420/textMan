from textblob import TextBlob
from translator import Translator

# Some Tags:
# C: conjunction, coordinating
# CD: numeral, cardinal
# DT: determiner
# IN: preposition or conjunction, subordinating
# JJ: adjective or numeral, ordinal
# NNP: noun, proper, singular


class Analyser(Translator):
    def __init__(self, text):
        super(Translator, self).__init__()
        self.text = text
        self.blob = TextBlob(self.text)
        self.analysis = None
        self.tags = None

    def analyse(self):
        self.analysis = self.blob.sentiment
        self.tags = self.blob.tags
        return

    def get_polarity(self):
        self.analyse()
        polarity_score = self.analysis.polarity
        return polarity_score

    def get_subjectivity(self):
        self.analysis()
        subjectivity_score = self.analysis.subjectivity
        return subjectivity_score

    def get_noun_phrases(self):
        noun_phrases = self.blob.noun_phrases
        return noun_phrases

    def get_tags(self, tag):
        tagged_words = []
        for tagset in self.tags:
            if tagset[1] == tag:
                tagged_words.append(tagset[0])
        return tagged_words



