
def most_frequent_char(lst):
    st=''.join(lst)
    d=dict()
    for a in st:
        if a not in d:
            d[a]=1
        else:
            d[a]+=1
    max_occurence = []
    for a in d:
        if d[a] == max(d.values()):
            max_occurence.append(a)
    return sorted(max_occurence)

