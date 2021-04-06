
from itertools import permutations as pt
​
def waterjug(s, goal):
    comb, lst, gen = list(pt([2, 1, 0],2)), [[[0, 0, s[2]]]], 0; cp ={str(lst[0][0]):0}
    if str(goal) in cp: return gen
    while len(lst[gen]) != 0:
        gen += 1; lst.append([])
        for i in lst[gen-1]:
            for j in comb:
                n = i[:]
                if n[j[0]] == 0: continue
                t= min(s[j[1]] - n[j[1]], n[j[0]]); n[j[1]] += t; n[j[0]] -= t
                if n == goal: return gen
                if str(n) not in cp: cp[str(n)] = gen; lst[gen].append(n)
    return "No solution."

