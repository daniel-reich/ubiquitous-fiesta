
def golomb(n):
    arr = [1] * (n+1) 
    for i in range(2, n+1):
        arr[i] = 1 + arr[i-arr[arr[i-1]]]  
    return arr[1:]

