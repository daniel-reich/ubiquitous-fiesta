
def k_th_binary_inlist(n, k):
    bin_list=[bin(x) for x in range (2**n)]
    bin_list.sort(key = number_of_ones, reverse = True)
    return bin_list[k-1]
    
def number_of_ones(x):
    return x.count("1")

