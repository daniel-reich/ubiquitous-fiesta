
def tune(lst):
    freq = [329.63, 246.94, 196, 146.83, 110, 82.41]
    res = []
    for x in range(len(lst)):
        if lst[x] == 0:
            res.append(' - ')
            continue
        diff = round((freq[x]) - lst[x] )/ lst[x] * 100
        if .5 >= diff >= -.5:
            res.append('OK')
        elif -0.5 > diff > -2.5:
            res.append('+<')
        elif diff <= -2.5:
            res.append('+<<')
        elif 0.5 < diff < 2.5:
            res.append('>+')
        elif diff >= 2.5:
            res.append('>>+')
    return res

