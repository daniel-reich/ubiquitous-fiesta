
def valid_division(d):
    l = list(map(lambda x:int(x),str(d).split("/")))
    return 'invalid' if l[1]==0 else l[0]%l[1]==0

