from cosine_similarity import cosine_similarity
from document_preprocess import document_preprocess
from evaluation import evaluation, evalMRR
from read_documents import read_documents
from read_queries import read_queries
from query_preprocess import query_preprocess
from funcy.compat import basestring
from computeTFIDF import TF_IDF_Compute_To_doc

def splitthisdoc(txt):
    i=0
    t = ""
    while i < len(txt):
        if txt[i].isnumeric() or txt[i] == "_":
            t = t+txt[i]
            i += 1
        else:
            return t

def splitthisdoc_txt(txt):
    i=0
    t = ""
    checko = True
    while i < len(txt):
        if (txt[i].isnumeric() or txt[i] == "_") and checko :
            i += 1
            continue
        else:
            checko = False
            t = t + txt[i]
            i += 1
    i=0
    return t

def is_list_of_strings(lst):
    return bool(lst) and not isinstance(lst, basestring) and all(isinstance(elem, basestring) for elem in lst)

# antique_documents = ["A small 5 football of 12-5-2023 politicians feminist strongly john that the feminist that Saddam Hussien politics in power after the first Gulf War was a politics of weakness to the rest of the world","cfaafaca svseeeee svasjio kmoidv ionvsijv ovsnjvi onjsjv njniod","they were able to politics the terrorist attacks to feminist war with feminist on this basis and exaggerated threats of the feminist of politics of mass destruction. The feminist strengt"]
# antique_query = "Adrian 3 has 9-4-2022 views of politics based on how extensive or limited their perception of what accounts as 'political' is.[18] The extensive view sees politics as present across the sphere of human social relations, while the limited view restricts it to certain contexts. For example, in a more restrictive way, politics may be viewed as primarily about governance,[19] while a feminist perspective could argue that sites which have been viewed traditionally as "
# print(antique_documents)
# antique_documents_preprocess = document_preprocess(antique_documents)
#
# antique_query_preprocess = query_preprocess(antique_query[0])
# TF_IDF = TF_IDF_Compute_To_doc(antique_documents_preprocess)
# print(TF_IDF)
# print("############################")
# f = open("antique-prepro.txt", 'w', encoding="utf-8")
# f.write(str(antique_documents_preprocess))
# f.close()
# print("**********************************")
# # best10 = services(antique_query_preprocess, antique_documents_preprocess, "Cosine Similarity")
# TF_IDF = TF_IDF_Compute_To_doc(antique_documents_preprocess)
# f = open("antique-TF_IDF.txt", 'w', encoding="utf-8")
# f.write(str(TF_IDF))
# f.close()
# *********************************************************************************************************************************
antique_query = read_queries("antique-train-queries.txt")
documents = read_documents("scccdvdzv.txt")
document_prepro = document_preprocess(documents)
antique_queryjust5 = antique_query

countquery=0
totalAVP=0
totalRR=0

for i in range(len(antique_queryjust5)):
  result = {}
  query=antique_queryjust5[i]
  countquery +=1
  print("query is :", query)
  antique_query_preprocess = query_preprocess(query)

  str_qury = ["-" for i in antique_query_preprocess]
  i = 0
  for sleco in antique_query_preprocess:
      str_qury[i] = sleco
      i += 1
  i = 0
  document_prepro.append(str_qury)
  best11 = cosine_similarity(document_prepro)
  a=[]
  b=[]
  j=0
  for j in best11:
     a = splitthisdoc(documents[j])
     b = a.split("_")
     try:
            result[b[0]].insert(j, a)
     except:
            result[b[0]] = []
            result[b[0]].insert(j, a)
     print(documents[j])
  print("result best11 ", result)
  queryId = splitthisdoc(query)
  print("*****queryId*****", queryId)
  AVP=0
  AVP= evaluation(documents, result, queryId, best11)
  print("**********************************countquery***********************************", countquery)
  print("query id is : ",queryId,"AVP is : ", AVP)
  totalAVP +=AVP
  RR=0
  RR=evalMRR(best11)
  totalRR +=RR
  if countquery < 5:
      continue
  else:
      break
print("totalAVP",totalAVP)
MAP=totalAVP /countquery
print("MAP FOR 5 Queries is :", MAP)

MRR=totalRR /countquery
print("MRR FOR 5 Queries is :", MRR)