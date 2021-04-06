
def diagonalize(n, d):
    l = [i for i in range(int(n+n*0.6+1))]
    final = []
    if d == "ul" or d == "ll":
        for j, k in enumerate(range(n)):
            final.append(list(l[j:n]))
            n += 1
    elif d == "ur" or "lr":
        for j, k in enumerate(range(n)):
            final.append(list(reversed(l[j:n])))
            n += 1  
    if d == "ll":
        final = sorted(final, reverse = True)
    elif d == "lr":
        final = sorted(final, reverse = True)
​
    return final

