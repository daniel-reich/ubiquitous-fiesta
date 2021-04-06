
def true_alphabetic(txt):
    lens = [len(i) for i in txt.split()]
    all_sorted = sorted(j for i in txt.split() for j in i)
    n = 0
    final = []
    for i in range(len(lens)): # 0, 1, 2
        final.append((str("".join(all_sorted[n : n + lens[i]])))) 
        n = n + lens[i]
    return " ".join(final)

