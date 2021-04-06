
def neutralise(s1, s2):
    dic = {"++":'+', "--":'-', "+-":'0',"-+":"0"}
    return "".join([dic[i+j] for i,j in zip(s1,s2)])

