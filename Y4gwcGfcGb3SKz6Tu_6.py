
def max_separator(txt):
    test = list(set(txt)); diff_max = []
    for i in test:
        p_i = [k for k, x in enumerate(txt) if x == i]
        if len(p_i) > 1:
            diff = [p_i[n] - p_i[n-1] for n in range(1,len(p_i))]
        else:
            diff = [0]
        diff_max.append(max(diff))
    
    result = [c for c, j in enumerate(diff_max) if j == max(diff_max) != 0]
    return sorted([test[n] for n in result])

