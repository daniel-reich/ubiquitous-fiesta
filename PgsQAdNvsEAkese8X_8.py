
def to_list(dct):
    dictolist = [[x, dct[x]] for x in dct]
    dictolist.sort() 
    return dictolist

