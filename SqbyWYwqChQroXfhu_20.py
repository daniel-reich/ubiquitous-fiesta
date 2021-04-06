
def lower_triang(arr):
    C=0
    for u in range(len(arr)-1):        
        for i in range(1,len(arr)):
            arr[u][i+C]=0
            if i+C==len(arr)-1:
                break
        C+=1        
    return arr

