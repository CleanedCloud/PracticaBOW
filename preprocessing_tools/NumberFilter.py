class NumberFilter:
    def filter(self, tokens):
        result = []
        for token in tokens:
            if self.is_not_number(token): result.append(token)
        return result

    def is_not_number(self, token: str):
        return not token.isnumeric()
