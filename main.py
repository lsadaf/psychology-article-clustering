import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import pandas as pd
from scipy import io

from sklearn.feature_extraction.text import TfidfVectorizer


df = pd.read_csv('D:/Data Mining/project/all_keywords300.csv')
total_documents = df['Keywords'][1:].tolist()



def add_to_doc_matrix(word, doc_num, count_docs):
    if word not in term_doc_matrix.keys():
        term_doc_matrix[word] = [0 for j in range(count_docs)]
    term_doc_matrix[word][doc_num] += 1


def get_doc_vector(tokenized_doc, dtm_key_list):
    dtm_len = len(dtm_key_list)
    vector = [0 for j in range(dtm_len)]
    for i in range(dtm_len):
        vector[i] += tokenized_doc.count(dtm_key_list[i])
    return vector

term_doc_matrix = {}

for i in range(len(total_documents)):
    for token in total_documents[i]:
        add_to_doc_matrix(token, i, 300)

dtm = pd.DataFrame.from_dict(term_doc_matrix)



dtm_dict = {}
for col in dtm.columns:
    dtm[col] = dtm[col].apply(lambda x: str(x).encode('cp1252'))
    

io.savemat('testmat.mat', dtm_dict)


#arr = [ "خدافظ","سلام"]

# Specify variable names for the .mat file
# variable_names = [str(col) for col in dtm.columns]
#
# # Prepare data for .mat file
# data = np.array(dtm.values.T, dtype=np.object)
#
# # Save data to .mat file
# sio.savemat('testmat.mat', {name: data[i] for i, name in enumerate(variable_names)})


#sio.savemat('array.mat', {'arr': arr})



# data dictionary
OutData = {}

# convert DF to dictionary before loading to your dictionary
# OutData['Obj'] = dtm.to_dict('list')

#io.savemat('testmat.mat', dtm)

def compute_tfidf(words_list):
    c = [' '.join(words) for words in words_list]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(c)
    return tfidf_matrix

#total_documents_tfidf = compute_tfidf(total_documents)

# c = np.array(dtm, dtype=np.object)
# sio.savemat('file.mat', {'cell' : c})
