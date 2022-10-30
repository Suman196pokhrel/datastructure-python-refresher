from unittest import result


def hourglasssum(arr):
    sum_arr = []
    for i in range(1,5):
        for j in range(1,5):
            sum_arr.append(arr[i][j] + (arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]) + (arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]))
    return max(sum_arr)





if __name__ == "__main__":
    arr = []
    for _ in range(6):
        arr.append(list(map(int,input().rstrip().split())))
    
    result = hourglasssum(arr)
    print(result)