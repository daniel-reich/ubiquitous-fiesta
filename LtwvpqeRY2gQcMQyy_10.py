
def sig_figs(num): #without regex
    a, p = [], num.find("."); ([a.append(i[0]) for i in enumerate(num) if i[1] not in "-.0"])
    return 0 if len(a)==0 else len(num[a[0]:])-1 if p > a[0] else a[-1]-a[0]+1 if p == -1 else len(num[a[0]:])

