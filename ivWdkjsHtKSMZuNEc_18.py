
def find_shortest_words(txt):
    import re
    txt = sorted(re.findall(r"[a-z\']+", txt.lower()), key=lambda x: len(x))
    return sorted(i for i in txt if len(i) == len(txt[0]))

