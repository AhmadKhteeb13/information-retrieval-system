def read_queries(query):
    f = open(query)
    queries = []
    for a_line in f.readlines(10000):
        temp2 = a_line.replace("\t", "")
        temp2.replace("\n", "")
        queries.append(temp2)

    return queries