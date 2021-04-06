
def mini_peaks(lst):
    alist = []
    for i in range(1,len(lst)-1):
        if lst[i-1] < lst[i] > lst[i+1]:
            alist.append(lst[i])
​
    return alist

