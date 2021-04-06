
def mini_peaks(lst):
    return [lst[a] for a in range(1,len(lst)-1) if lst[a-1]<lst[a]>lst[a+1]]

