
MAX = 100001
def golomb(N): 
    arr = [0] * MAX
    cnt = 0
    arr[0] = 0
    arr[1] = 1
    M = dict() 
    M[2] = 2
  
    for i in range(2, N + 1): 
        if (cnt == 0): 
            arr[i] = 1 + arr[i - 1] 
            cnt = M[arr[i]] 
            cnt -= 1
        else: 
            arr[i] = arr[i - 1] 
            cnt -= 1
        M[i] = arr[i] 
    return [arr[i] for i in range(1,N+1)]

