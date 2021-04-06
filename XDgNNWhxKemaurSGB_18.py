
def k_th_binary_inlist(n, k):
    lst = [format(0, "b")]
​
    for i in range(1, 2**n):
        lst.insert(0, format(i, "b"))
​
​
    return organize(lst)[k-1]
​
def getMaxOnes(lst):
    theMaxOfOnes = 0
​
    for i in lst:
        if i.count('1') > theMaxOfOnes:
            theMaxOfOnes = i.count('1')
​
    return theMaxOfOnes+1
​
def organize(lst):
    theMaxOfOnes  = getMaxOnes(lst)
    new_lst = []
​
    for i in range(theMaxOfOnes):
        new_lst.append([])
    
    for i in range(len(new_lst)):
        for j in range(len(lst)):
            if lst[j].count("1") == i:
                new_lst[i].append(lst[j])
​
    new_lst = [new_lst[i][::-1] for i in range(len(new_lst))][::-1]
​
    new_lst = [ '0b'+j for i in new_lst for j in i]
​
    return new_lst

