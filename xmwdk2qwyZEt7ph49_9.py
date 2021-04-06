
def get_length(lst):
    leng = 0
    for a in lst:
        if type(a)==list:
            leng += get_length(a)
        else:    
            leng += 1
    return leng

