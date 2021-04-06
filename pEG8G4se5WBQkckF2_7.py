
def reverse_sort(txt):
    return " ".join(sorted(txt.split(),
                           key=lambda w: (len(w), w.lower(), w[0].isupper()),
                           reverse=True))

