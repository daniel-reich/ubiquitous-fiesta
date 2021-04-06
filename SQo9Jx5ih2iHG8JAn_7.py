
def expanded_form(num):
    return ' + '.join([v+ "0"*(len(str(num))-i-1) for i,v in enumerate(str(num)) if v!="0"])

