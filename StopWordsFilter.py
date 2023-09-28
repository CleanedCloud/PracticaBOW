from nltk.corpus import stopwords


class StopWordsFilter:
    def __init__(self):
        super().__init__()

    def filter(self, tokens):
        result = []
        for token in tokens:
            if token not in stopwords: result.append(token)
        return result
