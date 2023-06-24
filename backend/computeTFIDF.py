from culc_number_of_documents import culc_number_of_documents
from doc_hava_this_word import doc_hava_this_word
from computeTF import term_freq
from computeDF import culc_DF
from culc_total_vocab import culc_total_vocab
from computeIDF import culc_IDF

def TF_IDF_Compute_To_doc(processed_text):

    number_of_documents = culc_number_of_documents(processed_text)
    TF = term_freq(processed_text)

    IDF = culc_IDF(processed_text)
    tf_idf = {}
    j=0
    for doc in processed_text:
        for sleco in doc:
            try:
                min_TF = TF.get(sleco)
                min_IDF = IDF.get(sleco)
                while j < number_of_documents:
                    tf_idf.setdefault(sleco, {})[j] = min_TF[j] * min_IDF[j]
                    j += 1
                j = 0
            except:
                continue
    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::TF_IDF:::::::::::::::::::::::::::::::::::::::::::::::::::")
    # for sloco in tf_idf:
    #     print(tf_idf.get(sloco))
    return tf_idf