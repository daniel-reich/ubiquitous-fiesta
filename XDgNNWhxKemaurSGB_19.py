
def get_len_of_ones(val):
    getbinary =lambda val : bin(val)[2:].count('1')
    return getbinary(val)
def k_th_binary_inlist(n,k):
    n=2**n
    myList=[i for i in range(n)]
    myTuple = zip(myList, map(get_len_of_ones,myList))
    sortedList = sorted(myTuple , key=lambda tup: tup[1],reverse=True)
    return bin(sortedList[k-1][0])

