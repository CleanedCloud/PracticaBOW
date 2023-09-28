import os

from DocxConverter import DocxConverter

converter = DocxConverter()
for file in os.listdir("data"):
    converter.convert_to_txt("data/" + file)
