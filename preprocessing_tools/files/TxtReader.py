class TxtReader:
    def read(self, file):
        with open(file, "r") as f:
            return f.read()
