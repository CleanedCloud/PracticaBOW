import numpy as np


class BowEncoder:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self.vocabulary_length = len(vocabulary)
        self.position_dict = self.position_dict()

    def encode(self, word):
        result = [0]*self.vocabulary_length
        result[self.get_index(word)] = 1
        return result

    def encode_text(self, token_list):
        result = np.zeros(self.vocabulary_length)
        for token in token_list:
            result += np.array(self.encode(token))
        return result.tolist()

    def get_index(self, word):
        return self.position_dict.get(word)

    def position_dict(self):
        return {word: pos for pos, word in enumerate(self.vocabulary)}