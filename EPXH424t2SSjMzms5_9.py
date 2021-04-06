
def remix(txt, lst):
    dic = {k:v for k,v in zip(lst, txt)}
    return "".join([v for k,v in sorted(dic.items(), key=lambda d: (d[0],d[1]))])

