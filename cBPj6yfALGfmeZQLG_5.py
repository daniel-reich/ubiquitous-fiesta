
def vertical_txt(txt):
    lst_words = txt.split()
    rows, cols = max(len(w) for w in lst_words), len(lst_words)
    return [[lst_words[c][r] if len(lst_words[c]) > r else ' '
             for c in range(cols)] for r in range(rows)]

