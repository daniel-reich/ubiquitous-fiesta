
def duplicate_count(txt):
    l = []
    for ch in txt:
        if txt.count(ch) > 1:
            if ch not in l:
                l.append(ch)
    return len(l)

