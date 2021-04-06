
def sentence_searcher(s, word):
    lst = s[:-1].split(". ")
    for st in lst:
        if word.lower() in st.lower():
            return "{}.".format(st)
    return ""

