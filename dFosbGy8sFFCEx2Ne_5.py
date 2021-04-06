
def rank(lst):
    '''
    Returns an R-style list of the ranking of elements in lst
    '''
    s_lst = sorted(lst)
    ranks = []
​
    for item in lst:
        count = lst.count(item)
        first = s_lst.index(item)
        ranks.append(round(sum(range(first,first+count))/count,1)) 
    
    return ranks

