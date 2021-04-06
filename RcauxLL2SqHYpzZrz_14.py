
def true_equations(lst):
    lst = list(i.split('=') for i in lst)
    new = list(zip((i[0] for i in lst), (i[1] for i in lst)))
    ans = []
    for pair in new:
        if eval(pair[0]) == int(pair[1]):
            ans.append('='.join(pair))
    return ans

