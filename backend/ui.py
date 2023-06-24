from flask import Flask , request , jsonify
from Crawler import Crawler
from computeDF import culc_DF
from cosine_similarity import cosine_similarity
from document_preprocess import document_preprocess
from funcy.compat import basestring
from query_preprocess import query_preprocess
from read_documents import read_documents
from computeTFIDF import TF_IDF_Compute_To_doc
from computeTF import term_freq
from computeIDF import culc_IDF

l = []

def is_list_of_strings(lst):
    return bool(lst) and not isinstance(lst, basestring) and all(isinstance(elem, basestring) for elem in lst)
def ir_search(searchdata):
    doc_url = ""
    documents = []
    tf = {}
    DF = {}
    IDF = {}
    result = {}
    TF_IDF = {}
    best10 = []
    if searchdata['antique'] == 'true':
        documents = read_documents("antique-prepro.txt")
        # documents = read_documents("antique-collection.txt")
    elif searchdata['wikIR1k'] == 'true':
        documents = read_documents("wikIR1k/documents.csv")
    document_prepro = document_preprocess(documents)
    # print(document_prepro)
    urls_to_visit = []
    result = document_prepro
    query = searchdata['query']
    query = query_preprocess(query)
    str_qury = ["-" for i in query]
    i = 0
    for sleco in query:
        str_qury[i] = sleco
        i += 1
    i = 0
    document_prepro.append(str_qury)
    if searchdata['tf'] == 'true':
        tf = term_freq(document_prepro)
        result = tf
    if searchdata['idf'] == 'true':
        IDF = culc_IDF(document_prepro)
        result = IDF
    if searchdata['tfidf'] == 'true':
        TF_IDF = TF_IDF_Compute_To_doc(document_prepro)
        result = TF_IDF
    if searchdata['cosinesimilarity'] == 'true':
        best10 = cosine_similarity(document_prepro)
        result = best10
    if searchdata['crawler'] == 'true':
        Crawler(urls=['http://www.bookofjoe.com/2005/11/worlds_most_exp.html','http://www.infopeople.org/search/chart.html']).run()

    if searchdata['df'] == 'true':
        DF = culc_DF(document_prepro)
        result = DF

    for i in result:
        l.append(documents[i])
    return l

app = Flask(__name__)

@app.route('/api/endpoint', methods=['POST'])
def handle_json():
    json_data = request.json
    response = ir_search(json_data)
    return jsonify(response)
@app.route('/',methods=['GET'])
def API():
    if request.method == 'GET':
        uri = 'https://www.brainyquote.com'
        return jsonify(l)

if __name__ == '__main__':
    app.run()