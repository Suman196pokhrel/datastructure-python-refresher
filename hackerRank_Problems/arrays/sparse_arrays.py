def matchingStrings(stringList, queries):
    freq_quer = []
    for quer in queries:
        c = 0
        for strings in stringList:
            if quer == strings:
                c +=1
        freq_quer.append(c)
    return freq_quer


if __name__ == '__main__':
    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    for i in res:
        print(i)
