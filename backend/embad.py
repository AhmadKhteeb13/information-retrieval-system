import warnings
warnings.filterwarnings(action = 'ignore')
from gensim.models import Word2Vec, KeyedVectors

def get_most_similar(word):
    embeddingMatrix = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
    jego = embeddingMatrix.most_similar(word)
    return jego

# embeddingMatrix = KeyedVectors.load_word2vec_format("antique-collection.txt", encoding="utf-8")
# print(embeddingMatrix)
# w1 = embeddingMatrix['king']
# w2 = embeddingMatrix['queen']
# w3 = embeddingMatrix['car']
#
# dist = np.linalg.norm(w1-w2,2)
# dist2 = np.linalg.norm(w1-w3,2)
#
# print("ww22", dist)
# print("ww33", dist2)

# print("Cosine similarity between 'alice' " + "and 'wonderland' - CBOW : ", model.most_similar('wonderland'))
# print("Cosine similarity between 'alice' " + "and 'machines' - CBOW : ", embeddingMatrix.most_similar('machines'))
# print("Cosine similarity between 'alice' " + "and 'wonderland' - Skip Gram : ",model.most_similar("glass"))
# print("Cosine similarity between 'alice' " + "and 'machines' - Skip Gram : ",model.most_similar("car"))
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# print(model.g)

