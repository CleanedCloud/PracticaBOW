from numpy import dot
from numpy.linalg import norm


class CosSimilarityDifference:
    def __init__(self, one_hot_text):
        self.one_hot_text_0 = one_hot_text

    def with_text(self, one_hot_text_1):
        return dot(self.one_hot_text_0, one_hot_text_1) / (norm(self.one_hot_text_0) * norm(one_hot_text_1))
