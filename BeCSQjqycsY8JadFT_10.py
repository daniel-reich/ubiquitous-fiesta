
def recur_index(txt, c='', i=0):
    if not txt: return {}
    if i > 0:
        return txt.find(c, i)
    cycle = ('', 0, len(txt))
    chrs = set()
    for j, ch in enumerate(txt):
        if j > cycle[2]: break
        if not ch in chrs:
            end = recur_index(txt, ch, j + 1)
            if end >= 0 and end < cycle[2]:
                cycle = (ch, j, end)
        chrs.add(ch)
    return {cycle[0]: [cycle[1], cycle[2]]} if cycle[0] else {}

