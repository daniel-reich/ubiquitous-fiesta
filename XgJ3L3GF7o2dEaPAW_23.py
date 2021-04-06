
def shared_letters(a, b):
    return ''.join(sorted(set([i for i in a.lower() if i in b.lower()])))

