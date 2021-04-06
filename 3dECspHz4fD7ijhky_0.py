
def numbers_range(ranges):
    if not ranges:
        return ''
    if len(ranges) == 1:
        return str(ranges[0])
​
    groups = [[ranges.pop(0)]]
​
    for i in ranges:
        if i - groups[-1][-1] == 1:
            groups[-1].append(i)
        else:
            groups.append([i])
            
    for idx, g in enumerate(groups):
        if len(g) >= 3:
            groups[idx] = '{}-{}'.format(g[0], g[-1])
        elif len(g) == 2:
            groups[idx] = '{}, {}'.format(g[0], g[1])
        else:
            groups[idx] = str(g[0])
            
    return ', '.join(groups)

