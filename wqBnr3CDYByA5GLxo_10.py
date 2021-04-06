
def unravel(txt,result=['']):
    if txt == '':
        return sorted(result)
    if txt[0] != '[':
        result = [i+txt[0] for i in result]
        return unravel(txt[1:],result)
    else:
        end = txt.index(']')
        lst = txt[1:end].split('|')
        result = [i+j for i in result for j in lst]
        return unravel(txt[end+1:],result)

