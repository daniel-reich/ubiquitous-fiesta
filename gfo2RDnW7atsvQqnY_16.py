
def count_smileys(lst):
    import re
    count = 0
    for s in lst:
        p = re.compile('^[:;][-~]?[)D]')
        m = p.match(s)
        if (m is None):
            continue
        count += 1
    return count

