
def best_friend(txt, a, b):
    return txt.count(''.join(a+b)) == txt.count(a)

