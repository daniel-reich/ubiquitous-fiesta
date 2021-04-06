
def split(txt,result=[]):
    d = {'(':1,')':-1}
    if txt == '': return result
    for i in range(len(txt)):
        if sum(d[j] for j in txt[:i+1]) == 0:
            return split(txt[i+1:],result+[txt[:i+1]])

