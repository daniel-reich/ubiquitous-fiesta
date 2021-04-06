
def check(d1, d2, k):
    try:
        return d1[k]==d2[k] or "Not the same"
    except KeyError:
        return "One's empty"

