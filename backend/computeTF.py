def how_much_word_in_doc(word , doc):
    i = 0
    for item in doc:
        if item == word:
            i += 1
    return i
def term_freq(documents ):
    sub = {}
    TF = {}
    i = 0
    j = 0
    for document in documents:
        for word in document:
            for document1 in documents:
                howmuch = how_much_word_in_doc(word , document1)
                TF.setdefault(word, {})[j] = howmuch / len(document1)

                j += 1
            j = 0
    # print("----------------------------------------------------TF-----------------------------------------------------")
    # for sleco in TF:
    #     print(sleco , TF.get(sleco))
    # print(TF)
    return TF