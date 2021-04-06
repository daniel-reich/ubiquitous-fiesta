
def lower_triang(arr):
    j=0
    for i in range(len(arr)-1,0,-1):
        arr[j] = arr[j][:j+1]+[0 for k in range(i)]
        j+=1
    return arr

