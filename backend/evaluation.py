import numpy as np
import cosine_similarity as cossimilarity
import document_preprocess
import read_documents
from read_queries import read_queries
from read_documents import read_documents

antique_documents = read_documents("scccdvdzv.txt")


def splitthisdoc(txt):
    i = 0
    t = ""
    while i < len(txt):
        if txt[i].isnumeric() or txt[i] == "_":
            t = t + txt[i]
            i += 1
        else:
            return t

def evaluation(doc_set,best,qId,best10):
    rel_set = {}
    with open('antique-train.qrel.txt') as f:
        for l in f.readlines():
            a = l.split()
            qry_id=a[0]
            doc_id=a[2]
            if qry_id in rel_set:
                rel_set[qry_id].append(doc_id)
            else:
                rel_set[qry_id] = []
                rel_set[qry_id].append(doc_id)

    resultTruth={}
    j=0
    for i in rel_set:
        if i.__eq__(qId):
                for j in range(len(rel_set[i])):
                    try:
                        resultTruth[i].append(rel_set[i][j])
                        j += 1
                    except:
                        resultTruth[i] = []
                        resultTruth[i].append(rel_set[i][j])
                        j += 1
    print("result Truth for query : ", resultTruth)
    k=0
    j=0
    i=0

    k=0
    i=0
    j=0
    bestAll={}
    print("best  :  ",best)
    for i in best:
        for j in range(len(best[i])):
                try:
                    bestAll[k].append(best[i][j])
                    j += 1
                except:
                    bestAll[k] = []
                    bestAll[k].append(best[i][j])
                    j += 1
    print("bestAll  : ",bestAll)

    k = 0
    j = 0
    i = 0

    for i in resultTruth:
     for j in bestAll:
        if i.__eq__(qId):
          true_Positive = len(set(bestAll[j]) & set(resultTruth[i]))
          false_Positive = len(np.setdiff1d(bestAll[j], resultTruth[i]))
          false_Negative = len(np.setdiff1d(resultTruth[i], bestAll[j]))
          true_negative = (len(doc_set) - (true_Positive + false_Negative + false_Positive))

          print("set(result_from_ground_truth)", set(resultTruth[i]))
          print(" set(best): ", set(bestAll[j]))
          print("::::::::::::::::::::::", true_Positive)
          print(":::::::::::::::::::::::::::::::::::::::::::", false_Positive)
          print("<<<<<<<:::::::::::::::::::::::::::::::::::::::::::>>>>>>>", false_Negative)


          precission = (true_Positive) / (true_Positive + false_Positive)
          recall = (true_Positive) / (true_Positive + false_Negative)
          print("Precision is : ", precission)
          print("Recall is : ", recall)
        else:continue


    retrievdREL={}
    for i in best:
        if i.__eq__(qId):
                for j in range(len(best[i])):
                    try:
                        retrievdREL[i].append(best[i][j])
                        j += 1
                    except:
                        retrievdREL[i] = []
                        retrievdREL[i].append(best[i][j])
                        j += 1
    print("*********************retrievdREL*****************", retrievdREL)

    # antique_documents = read_documents("scccdvdzv.txt")

    # def splitthisdoc(txt):
    #     i = 0
    #     t = ""
    #     while i < len(txt):
    #         if txt[i].isnumeric() or txt[i] == "_":
    #             t = t + txt[i]
    #             i += 1
    #         else:
    #             return t

    i=0
    k=0
    trueRANKRES={}
    for i in best10:
        a = splitthisdoc(antique_documents[i])
        try:
            trueRANKRES[k].append(a)

        except:
            trueRANKRES[k] = []
            trueRANKRES[k].append(a)
    print("*********************trueRANKRES*****************", trueRANKRES)

    AVP = 0.0
    sum=0.0
    k=0
    i=0
    for i in retrievdREL:
        for l in trueRANKRES:
            for j in range(len(retrievdREL[i])):
              h=j+1
              for k in range(len(trueRANKRES[l])):
                if retrievdREL[i][j].__eq__(trueRANKRES[l][k]):
                  k+=1
                  sum +=h/k
                  k=0
                  break
    AVP=sum/(true_Positive + false_Positive)
    print("true_Positive is : ", true_Positive)
    print("false_Positive is : ", false_Positive)
    print("sum is : ", sum)
    print("AVP is : ", AVP)

    return AVP

def evalMRR(best10):
    rel_set = {}
    RR=0
    with open('antique-train.qrel.txt') as f:
        for l in f.readlines():
            a = l.split()
            qry_id = a[0]
            doc_id = a[2]
            if qry_id in rel_set:
                rel_set[qry_id].append(doc_id)
            else:
                rel_set[qry_id] = []
                rel_set[qry_id].append(doc_id)
    # antique_documents = read_documents("scccdvdzv.txt")

    # def splitthisdoc(txt):
    #     i = 0
    #     t = ""
    #     while i < len(txt):
    #         if txt[i].isnumeric() or txt[i] == "_":
    #             t = t + txt[i]
    #             i += 1
    #         else:
    #             return t

    i = 0
    k = 0
    trueRANKRES = {}
    for i in best10:
        a = splitthisdoc(antique_documents[i])
        try:
            trueRANKRES[k].append(a)

        except:
            trueRANKRES[k] = []
            trueRANKRES[k].append(a)
    print("*********************trueRANKRES*****************", trueRANKRES)

    reciprocal_ranks = []
    for k in trueRANKRES:
        for docId in trueRANKRES[k]:  # first result doc in cos reteieved
            for j in rel_set:
                # if j.__eq__(k):
                for i, doc in enumerate(rel_set[j]):
                    if doc.__eq__(docId):
                        # print(doc, "  ", docId, "iiiiiiiiiiiiiiiiiii", i )
                        reciprocal_ranks.append(1 / (i+1 ))
                        RR = np.sum(reciprocal_ranks)
                        break
                    if RR != 0:
                        break
        if RR != 0:
            break
    print("RR: ", RR)

    return RR
