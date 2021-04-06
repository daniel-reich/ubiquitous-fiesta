
def recur_index(txt,index=0):
    if not txt or index  == len(txt):
        return {}
    if txt[index] in txt[:index]:
        return {txt[index]: [txt.index(txt[index]), index]}
    
    return recur_index(txt, index+1)

