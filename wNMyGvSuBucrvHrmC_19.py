
def number_of_repeats(s):
    newd = {}
    for i in s:
        if i not in newd:
            newd[i] = 1
        else:
            newd[i] += 1 
    return newd[s[0]]

