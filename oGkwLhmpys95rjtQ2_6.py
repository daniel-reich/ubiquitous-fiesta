
def match_last_item(lst):
    return ''.join(list(map(lambda x:str(x),lst[0:len(lst) - 1]))) == lst[-1]

