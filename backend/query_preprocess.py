from textblob import TextBlob , Word
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from dateutil.parser import parse
from num2words import num2words
from datetime import date
def is_date(string, fuzzy=False):
    if string.find("-") != -1 or string.find("_") != -1 or string.find("/") != -1 or string.find("(") != -1 or string.find(")") != -1 or string.find("'") != -1:
        try:
            parse(string, fuzzy=fuzzy)

        except ValueError:
            return False
    else:return False

def query_preprocess(text):
    punc = "!()-[]{};:'\"\\,<>./?@#$%^&*_~"
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    all_tokens = []
    if ' ' in text:
        temp = text.lstrip('0123456789.- ,_')
        temp2 = temp.replace("\t", "")
        text = temp2.replace("\n", "")

        tokens = text.split(" ")
        tokens2 = []
        for token in tokens:
            token = token.lower()
            # if token in ("SYM", "LS", ".", "!", "?", ",", ":", "(", ")", "\"", "#", "$"):
            #     continue
            if token in punc:
                continue
            else:
                if is_date(token):
                    t = ""
                    daty = [0, 0, 0]
                    k = 0
                    u = 0
                    while k < len(token):
                        if token[k].isnumeric():
                            t = t.__add__(token[k])
                        else:
                            daty[u] = t
                            t = ""
                            u += 1
                        k += 1
                    daty[u] = t
                    k = 0
                    u = 0
                    s = date(day=int(daty[0]), month=int(daty[1]), year=int(daty[2])).strftime('%A %d %B %Y')
                    ss = s.split(' ')
                    for slico in ss:
                        if u == 1 or u == 3:
                            tokens2.append(num2words(int(slico)).lower())
                        else:
                            tokens2.append(slico.lower())
                        u += 1
                    u = 0
                else:
                    if token.isnumeric():
                        tokens2.append(num2words(int(token)))
                    word_lemmatized = lemmatizer.lemmatize(token, pos='n')
                    tb_word = TextBlob(word_lemmatized)
                    tb_word = tb_word.correct()
                    if tb_word.tags != []:
                        if tb_word.tags[0][1] == "NN":
                            tokens2.append(token)
                        # token = Term_correct(token)
                        elif tb_word.tags[0][0] not in stop_words:
                            # token = lemmatizer.lemmatize(token)
                            token = stemmer.stem(tb_word.tags[0][0])
                            tokens2.append(token)

        return tokens2
    else:
        if text not in ("SYM", "LS", ".", "!", "?", ",", ":", "(", ")", "\"", "#", "$"):
            tokens2 = []
            if is_date(text):
                t = ""
                daty = [0, 0, 0]
                k = 0
                u = 0
                while k < len(text):
                    if text[k].isnumeric():
                        t = t.__add__(text[k])
                    else:
                        daty[u] = t
                        t = ""
                        u += 1
                    k += 1
                daty[u] = t
                k = 0
                u = 0
                s = date(day=int(daty[0]), month=int(daty[1]), year=int(daty[2])).strftime('%A %d %B %Y')
                ss = s.split(' ')
                for slico in ss:
                    if u == 1 or u == 3:
                        tokens2.append(num2words(int(slico)).lower())
                    else:
                        tokens2.append(slico.lower())
                    u += 1
                u = 0
            else:
                if text.isnumeric():
                    tokens2.append(num2words(int(text)))
                text = Term_correct(text)
                if text not in stop_words:
                    token = lemmatizer.lemmatize(text)
                    token = stemmer.stem(token)
                    tokens2.append(token)
        return tokens2


def Term_correct(word):
    text = TextBlob(word)
    s = text.correct()
    return s