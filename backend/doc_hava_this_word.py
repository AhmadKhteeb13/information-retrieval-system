def doc_hava_this_word(processed_text):
    Counter_word = {}
    for i in range(len(processed_text)):
        tokens = processed_text[i]
        for w in tokens:
            try:
                Counter_word[w].add(i)
            except:
                Counter_word[w] = {i}
    # print(":::::::::::::::::::::::::::::::::::::::::::::::Counter_word::::::::::::::::::::::::::::::::::::::::::::::::")
    # print(Counter_word)
    return Counter_word