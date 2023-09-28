import os
from DocxConverter import DocxConverter
from TxtPreprocesser import TxtPreprocesser
from TxtReader import TxtReader

converter = DocxConverter()
reader = TxtReader()
preprocesser = TxtPreprocesser(reader)
texts = []

for file in os.listdir("data"):
    converter.convert_to_txt("data/" + file)

for file in os.listdir("datatxt"):
    texts.append(preprocesser.preprocess("datatxt/" + file))