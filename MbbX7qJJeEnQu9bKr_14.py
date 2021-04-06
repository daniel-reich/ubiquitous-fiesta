
def max_occur(text):
    c = max(text.count(x) for x in set(text))
    s = [x for x in set(text) if text.count(x) == c and c > 1]
    return sorted(s) if s else "No Repetition"

