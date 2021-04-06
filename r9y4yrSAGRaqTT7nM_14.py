
def find_missing(lst):
    x=[]
    if not lst:
        return False
    for i in range(len(lst)):
        if len(lst[i]) == 0:
            return False
        else:
            return [i for i in range(min([len(i) for i in lst]),max([len(i) for i in lst])) if i not in [len(i) for i in lst]][0]

