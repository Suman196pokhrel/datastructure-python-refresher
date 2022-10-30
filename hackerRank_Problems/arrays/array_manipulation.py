def arrayManipulation(n, queries):
    arr = [0 for _ in range(n)]

    # prefix Sum algorithm
    for quer in queries:
        a,b,k = quer
        arr[a-1] += k
        arr[b] -= k

    sum = res = 0
    for elem in arr:
        sum +=elem
        if sum > res:
            res = sum

    return res




if __name__ == '__main__':
   
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    print(result)