from computeTF import term_freq
from doc_hava_this_word import doc_hava_this_word

def culc_DF(processed_text):
    Counter_word = doc_hava_this_word(processed_text)
    DF = {}
    for i in Counter_word:
        try:
            DF[i] = len(Counter_word[i])
        except:
            continue
    # print("::::::::::::::::::::::::::::::::::::::::::::::::::::DF:::::::::::::::::::::::::::::::::::::::::::::::::::::")
    # for sleco in DF:
    #     print(sleco , DF.get(sleco))
    # print(DF)
    return DF