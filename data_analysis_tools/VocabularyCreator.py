class VocabularyCreator:
    def from_text_list(self, text_list):
        result = []
        for token_list in text_list:
            for token in token_list:
                result.append(token)
        return set(result)

