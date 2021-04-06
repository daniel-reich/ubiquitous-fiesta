
def dakiti(lyrics):
    return ' '.join([remove_number(x) for x in sorted(lyrics.split(' '),key = get_number)])
    
​
​
​
​
​
def get_number(aword):
    for eachnumber in aword:
        if eachnumber.isdigit():
            return int(eachnumber)
        
        
def remove_number(aword):
    emptystring = ''
    for eachletter in aword:
        if eachletter.isdigit():
            continue
        else:
            emptystring += eachletter
    return emptystring

