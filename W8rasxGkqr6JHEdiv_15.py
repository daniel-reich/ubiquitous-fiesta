
from itertools import combinations_with_replacement as comb
from itertools import permutations as perm
def countdown(ope, tar):
    num = [i for i in perm([str(i) for i in list(ope)], r = len(ope))]
    sym = ['+', '-', '*', '//']*(len(ope)-1)
    com = [i for i in comb(sym, len(ope)-1) if len(i) == len(ope)-1]
    res = []; aux = []
    for i in num:
        for j in com:
            for el, k in enumerate(j):
                aux += [i[el], k]
            aux += [i[el+1]]; res.append(aux); aux = []
    end = [''.join(i) for i in res]
    for i in end:
        if eval(i) == tar: return i

