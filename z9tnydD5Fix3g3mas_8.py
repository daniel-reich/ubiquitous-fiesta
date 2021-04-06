
def pat(x):
    val = 0
    vals = []
    for i in range(len(x)):
        if i == 0 or x[i] not in x[:i]:
            vals.append(val)
            val += 1
        else:
            vals.append([vals[j] for j in range(len(vals)) if x[i] == x[j]][0])
    return vals
​
def check_pattern(lst, pattern):
    return pat(lst) == pat(pattern)

