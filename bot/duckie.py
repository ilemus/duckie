'''
Duckie is a bot that implements the Bot interface.
'''
from typing import List
import pyphen
import nltk

from bot.bot import Bot


class Duckie(Bot):
    def __init__(self, name):
        self.name = name
        self.phen = pyphen.Pyphen(lang='en')
        nltk.download('punkt')

    def _tokenize(self, message) -> List[str]:
        # Tokenize the message into a list of words and then split the words by syllables using the Pyphen library
        words = nltk.word_tokenize(message)
        # Remove symbols from the words
        tokens = list()
        for word in words:
            if word.isalpha():
                if tokens:
                    tokens.append(' ')
                tokens.extend(self.phen.inserted(word).split('-'))
        return tokens


    def prompt(self, message) -> str:
        tokens = self._tokenize(message)
        

        return "Woof"
