import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn

from data_analysis_tools.CosSimilarityDifference import CosSimilarityDifference
from preprocessing_tools.files.DocxConverter import DocxConverter
from data_analysis_tools.Kmeans import Kmeans
from preprocessing_tools.Lowerizer import Lowerizer
from preprocessing_tools.NumberFilter import NumberFilter
from data_analysis_tools.BowEncoder import BowEncoder
from preprocessing_tools.PunctuationRemover import PunctuationRemover
from preprocessing_tools.StopWordsFilter import StopWordsFilter
from preprocessing_tools.Tokenizer import Tokenizer
from preprocessing_tools.files.TxtReader import TxtReader
from data_analysis_tools.VocabularyCreator import VocabularyCreator


converter = DocxConverter()
for file in os.listdir("data"):
    converter.convert_to_txt("data/" + file)

preprocessed_texts = []
for file in os.listdir("datatxt"):
    text = TxtReader().read("datatxt/" + file)
    lowerized_text = Lowerizer().lower(text)
    lowerized_without_punctuation_text = PunctuationRemover().remove(lowerized_text)
    tokenized_text = Tokenizer().tokenize(lowerized_without_punctuation_text)
    filtered_tokenized_text = StopWordsFilter().filter(tokenized_text)
    without_number_filtered_tokenized_text = NumberFilter().filter(filtered_tokenized_text)
    preprocessed_texts.append(without_number_filtered_tokenized_text)

vocabulary = VocabularyCreator().from_text_list(preprocessed_texts)
encoder = BowEncoder(vocabulary)
result = []
for text in preprocessed_texts:
    result.append(encoder.encode_text(text))

matrix = []
for text_0 in result:
    cos_similarity_dif = CosSimilarityDifference(text_0)
    row = []
    for text_1 in result:
        row.append(cos_similarity_dif.with_text(text_1))
    matrix.append(row)
print(np.array(matrix))

df_cm = pd.DataFrame(matrix, ["Text{}".format(i) for i in list(range(1, 13))],
                     ["Text{}".format(i) for i in list(range(1, 13))])
sn.set(font_scale=1.4)
sn.heatmap(df_cm, annot=True, annot_kws={"size": 16})
plt.title("Similitud entre documentos")
plt.show()


labels_custom = Kmeans().create_clusters(np.array(matrix), 4)
clustered_texts_custom = list(zip(["Text{}".format(i) for i in list(range(1, 13))], labels_custom))

print(clustered_texts_custom)
