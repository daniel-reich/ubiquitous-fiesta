
def bracket_logic(xp):
    c = [40,41,60,62,91,93,123,125]
    
    temp = ''
    for item in xp:
        if ord(item) in c:
            temp += item
    chk = True
    while len(temp) > 0 and chk == True:
        chk = False
        if '[]' in temp:
            temp = temp.replace('[]','')
            chk = True
        if '{}' in temp:
            temp = temp.replace('{}','')
            chk = True
        if '()' in temp:
            temp = temp.replace('()','')
            chk = True
        if '<>' in temp:
            temp = temp.replace('<>','')
            chk = True
    
    if len(temp) == 0:
        return True
    return False

