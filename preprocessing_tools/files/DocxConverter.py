import docx2txt


class DocxConverter:
    def __init__(self):
        super().__init__()

    def convert_to_txt(self, docxFile):
        text = docx2txt.process(docxFile, self.name(docxFile))
        with open(self.name(docxFile), "w") as f: f.write(text)

    def name(self, docxFile):
        return docxFile.split("/")[0] + "txt" + "/" + docxFile.split("/")[1].split(".")[0] + ".txt"

