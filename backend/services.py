from Crawler import Crawler
from culc_number_of_documents import culc_number_of_documents
from computeTFIDF import TF_IDF_Compute_To_doc
from cosine_similarity import cosine_similarity
import array
from embad import get_most_similar
def services(query, processed_text, algorithm):
    number_of_documents = culc_number_of_documents(processed_text)
    # range = (len(query))*2
    # str_qury = array.array('f', [0] * (range))
    str_qury = []

    for sleco in query:
        str_qury.append(sleco)
    print("****************",get_most_similar(str(str_qury[4])))
    # doc_with_qury = processed_text.append(str_qury)
    # print(processed_text)
    # doc_TF_IDF = TF_IDF_Compute_To_doc(processed_text)
    if algorithm == "TFIDF":
        print()
        return 10
    elif algorithm == "Cosine Similarity":
        print()
        # best10 = cosine_similarity(doc_TF_IDF, number_of_documents)
        # return best10
        return 10
    elif algorithm == "Crawler":
        Crawler(urls=['https://medium.com/@razvantmz/database-for-dart-frog-b21089dac1b2']).run()
        return 10