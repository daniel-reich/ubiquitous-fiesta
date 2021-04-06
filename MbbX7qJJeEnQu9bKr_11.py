
def max_occur(text):
    dict = {}
    for i in text:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    m = max(dict.values())
    if m < 2:
        return 'No Repetition'
    else:
        myans = []
        for k,v in dict.items():
            if v == m:
                myans.append(k)
    return sorted(myans)

