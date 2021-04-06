
def count_ones(binVal):
    return binVal.count("1")
​
def k_th_binary_inlist(n, k):
    binList = [bin(i) for i in range(2 ** n)]   
    binList.sort(reverse=True, key=count_ones)
    return binList[k-1]

