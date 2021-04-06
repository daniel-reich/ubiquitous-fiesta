
def longest_nonrepeating_substring(txt):
    l_run = []
    cur_longest = []
    for i in txt:
        if i not in l_run:
            l_run.append(i)
        else:
            if len(l_run) > len(cur_longest):
                cur_longest = l_run[:]
            l_run.append(i)
            del l_run[:l_run.index(i) + 1]
    if len(l_run) > len(cur_longest):
        cur_longest = l_run
    return ''.join(cur_longest)

