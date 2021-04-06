
def join(lst):
    overlaps =[max(set([p[i:] for i in range(len(p))]) & set([w[:i+1] for i in range(len(w))]),key=len, default='') for p, w in zip(lst,lst[1:])]
    return [lst[0] + ''.join([w[len(o):] for o, w in zip(overlaps,lst[1:])]), len(min(overlaps,key=len))]

