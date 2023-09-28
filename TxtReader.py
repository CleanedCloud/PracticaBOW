class TxtReader:

    def read(self, file):
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()
        return text