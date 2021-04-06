
def shared_letters(a, b):
    return "".join(sorted(set(a.lower()) & set(b.lower())))

