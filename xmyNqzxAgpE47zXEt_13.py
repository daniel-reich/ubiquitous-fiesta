
def is_alphabetically_sorted(txt):
    import string
    txt_clean = txt.translate(str.maketrans('', '', string.punctuation)).split(" ")
    sorted_txt = ["".join(sorted(txt_clean[i])) for i in range(0,len(txt_clean))]
    txt_compare = [sorted_txt[i] == txt_clean[i] and len(txt_clean[i])>=3 for i in range(0,len(sorted_txt))]
    return any(txt_compare)

