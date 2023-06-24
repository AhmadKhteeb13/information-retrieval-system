import array
import numpy as np
from computeTFIDF import TF_IDF_Compute_To_doc
from culc_number_of_documents import culc_number_of_documents
def cosine_sim(a, b):
    # print("****************************",a)
    cos_sim = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return cos_sim

def cosine_similarity(processed_text):
    TF_IDF = TF_IDF_Compute_To_doc(processed_text)
    number_of_doc = (culc_number_of_documents(processed_text))-1
    # print(number_of_doc)
    qury = [0 for i in TF_IDF]
    i = 0
    for sleco in TF_IDF:
        qury[i] = TF_IDF.get(sleco).get(number_of_doc)
        i += 1
    i = 0
    j =0
    # a = array.array('f',[0]*5)
    d_cosines = array.array('f',[0]*(number_of_doc))

    tem_doc = [0 for i in TF_IDF]
    while i < (number_of_doc):
        for sleco in TF_IDF:
            tem_doc[j] = TF_IDF.get(sleco).get(i)
            j += 1
        j = 0
        d_cosines[i] = cosine_sim(qury, tem_doc)
        i += 1
    i = 0
    j = 0
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Cosine Similarity~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print(d_cosines)
    out = np.array(d_cosines).argsort()[-10:][::-1]
    return out