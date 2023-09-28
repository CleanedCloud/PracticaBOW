from Lowerizer import Lowerizer

class TxtPreprocesser:
    def __init__(self, reader):
        self.reader = reader

    def preprocess(self, file):
        return Lowerizer().lower(self.reader.read(file))
