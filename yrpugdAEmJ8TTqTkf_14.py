
def secret(num):
    n = list(map(lambda x:int(x), list(str(num))))
    return n[0]**n[1] - n[0]*n[1]

