from datetime import date
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from textblob import TextBlob, Word
from num2words import num2words
from dateutil.parser import parse
import sys

def is_date(string, fuzzy=False):
    if string.find('/') == -1  and string.find('-') == -1  and string.find('\'') == -1  and string.find('_') == -1    :
        if string.find("-") != -1 or string.find("_") != -1 or string.find("/") != -1 or string.find(
                "(") != -1 or string.find(")") != -1 or string.find("'") != -1:
            if float(string) >= sys.maxsize:
                return False
            try:
                parse(string, fuzzy=fuzzy)
            except ValueError:
                return False
        else:
            return False
    else:return False


def document_preprocess(text):
    all_tokens = []
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    symbols = "!\"#$\'%&()*+-./:;<=>?@[]^_`{|}~½¼²¾½=<>↉⅓⅔¼¾⅕?⅖⅗⅘⅙⅚⅐\⅛⅜⅝⅞⅑⅒\n"
    for item in text:
        temp = item.lstrip('0123456789.- ,_')
        item = temp.replace("\t", "")

        tokens = [word.lower() for word in nltk.word_tokenize(item)]
        tokens2 = []
        for token in tokens:
            if token not in stop_words:
                if token in (
                "SYM", "'", "-", "''", "``", "LS", ".", "!", "?", ",", ":", "(", ")", "\"", "#", "$", "...", "--", ";",
                "{", "}", "`", "½", "¼", '²', '2²', "", 'id_right', 'text_right', ''):
                    continue
                else:
                    for i in range(len(symbols)):
                        token = token.replace(symbols[i], '')

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
                        if token.isnumeric() and len(token) < 100:
                            tokens2.append(num2words(int(token)).lower())
                        else:
                            if token != "":
                                word_lemmatized = lemmatizer.lemmatize(token, pos='n')
                                tb_word = TextBlob(word_lemmatized)
                                tb_word = tb_word.correct()
                                if tb_word.tags[0][1] == "NN":
                                    tokens2.append(token)
                                else:
                                    token = stemmer.stem(tb_word.tags[0][0])
                                    tokens2.append(token)

        all_tokens.append(tokens2)
    return all_tokens
#
# def Term_correct(word):
#     text = TextBlob(word)
#     s = text.correct()
#     return s