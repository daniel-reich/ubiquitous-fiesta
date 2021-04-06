
def order(lst):
    '''
    Returns a list of R-style indices needed to sort lst.
    '''
    return [i for _,i in sorted([(item,i) for i,item in enumerate(lst)])]

