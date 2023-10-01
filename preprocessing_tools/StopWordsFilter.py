import nltk


class StopWordsFilter:
    def __init__(self):
        super().__init__()

    def filter(self, tokens):
        result = []
        for token in tokens:
            if token not in nltk.corpus.stopwords.words('spanish'): result.append(token)
        return result
