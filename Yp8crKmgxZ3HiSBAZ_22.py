
def freq_count(arr, el):
    string = str(arr)
    nesting = -1
    highest_nesting = 0
    res_dict = {}
    res = []
    for c in string:
        if c == '[':
            nesting += 1
            highest_nesting = max(highest_nesting, nesting)
        elif c == ']':
            nesting -= 1
        elif c == ' ' or c == ',':
            continue
        else:
            num = int(c)
            if num == el:
                if nesting in res_dict:
                    res_dict[nesting] += 1
                else:
                    res_dict[nesting] = 1
    for i in range(highest_nesting+1):
        if i in res_dict:
            res.append([i, res_dict[i]])
        else:
            res.append([i, 0])
    return res

