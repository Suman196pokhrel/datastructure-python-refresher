from ctypes import sizeof


def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    answers = []
    lastAnnswer = 0
    for quer in queries:
        a,x,y = quer
        idx = (x^lastAnnswer)%n
        if a ==1:
            arr[idx].append(y)
        elif a == 2:
           
            lastAnnswer =  arr[idx][y% len(arr[idx])]
            answers.append(lastAnnswer)
    return answers





if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print(result)