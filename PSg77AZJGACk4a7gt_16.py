
def meme_sum(a, b):
    l = max(len(str(a)),len(str(b)))
    a = list(str(a).zfill(l))
    b = list(str(b).zfill(l))
    return int(''.join(list(map(lambda x:str(sum(list(map(lambda y:int(y),x)))),list(zip(a,b))))))

