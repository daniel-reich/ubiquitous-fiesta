
def freq_count(lst, el):
    res = str(lst).replace(',', '').replace(' ', '')
    for i in range(10):
        if i != el:
            res = res.replace(str(i), '')
    level, max_level = 0, 0
    level_freq = {}
    for c in res[1:-1]:
        if c == str(el):
            if level not in level_freq:
                level_freq[level] = 1
            else:
                level_freq[level] += 1
        elif c == '[':
            level += 1
            if max_level < level:
                max_level = level
        elif c == ']':
            level -= 1
    for level in range(max_level + 1):
        if level not in level_freq:
            level_freq[level] = 0
    return sorted([[k, v] for k, v in level_freq.items()])

