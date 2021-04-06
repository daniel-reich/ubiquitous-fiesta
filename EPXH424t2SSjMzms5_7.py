
def remix(txt, lst):
    myDict = {k:v for k,v in zip(lst,list(txt))}
    return ''.join([myDict[x] for x in sorted(myDict)])

