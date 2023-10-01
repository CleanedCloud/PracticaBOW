import string


class PunctuationRemover:
    def __init__(self):
        super().__init__()

    def remove(self, text):
        result = ""
        for char in text:
            if char not in string.punctuation + "\n": result += char
        return result
