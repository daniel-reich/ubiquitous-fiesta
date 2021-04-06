
def next_element(lst):
    lengthList = len(lst)
    return formula(lst, lengthList)
    
def formula(lst,numTerms):
    firstTerm = lst[0]
    Difference = lst[1]-lst[0]
    nextTermIndex = numTerms + 1
    x_index = firstTerm + Difference*(nextTermIndex-1)
    return x_index

