def rotateLeft(d, arr):
    for _ in range(d):
        temp, arr = arr[0],arr[1:]
        arr.append(temp)
    return arr


def rotateLeft_1(d, arr):
    return arr[d:]+arr[:d]






if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = rotateLeft(d, arr)
    print(result)
