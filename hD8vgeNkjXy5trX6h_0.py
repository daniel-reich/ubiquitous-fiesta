
def combo(lst, n):
    if n==0:
        return [[]]
    elif n>len(lst):
        return []
    elif lst==[]:
        return [] 
    else:
        combos = []
        for i in range(0, len(lst) ):
            old_combos = combo(lst[i+1:len(lst)],n-1)
            for j in old_combos:
                combos += [ [lst[i]] + j ]
        return combos

