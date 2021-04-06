
def unique_abbrev(abbs, words):
    count,lst=0,[]
    for i in words:
        for j in abbs:
            if i.startswith(j):
                lst.append(i)
    return len(lst)==len(words)

