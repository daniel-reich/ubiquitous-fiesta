
def sums_up(lst):
    l = [[lst[j], lst[i]] for i in range(len(lst) -1) for j in range(i+1, len(lst)) if lst[i] + lst[j] == 8]
    return {'pairs': [sorted(i) for i in sorted(l, key=lambda x: lst.index(x[0]))]}

