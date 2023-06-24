
def read_documents(txt):
    f = open(txt,encoding="utf-8")
    documents = []
    for a_line in f.readlines():
        documents.append(a_line.replace("\t",""))
    return documents


