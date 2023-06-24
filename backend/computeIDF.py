import numpy as np
from computeDF import culc_DF
from computeTF import term_freq
from culc_number_of_documents import culc_number_of_documents

def culc_IDF(processed_text):
    number_of_documents = culc_number_of_documents(processed_text)
    # TF = term_freq(processed_text)
    DF = culc_DF(processed_text)
    IDF = {}
    j = 0
    for i in DF:
        while j < number_of_documents:
            IDF.setdefault(i, {})[j] = np.log(abs(number_of_documents / (DF[i])))
            j += 1
        j = 0
    # print("::::::::::::::::::::::::::::::::::::::::::::::::::::IDF::::::::::::::::::::::::::::::::::::::::::::::::::::")
    # for sleco in IDF:
    #     print(IDF.get(sleco))
    # print(IDF)
    return IDF