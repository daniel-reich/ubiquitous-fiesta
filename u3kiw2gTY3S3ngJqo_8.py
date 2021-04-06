
def superheroes(n):
    a = list(filter(lambda x : x.lower().endswith('man'), n))
    b = list(filter(lambda x : x.lower().endswith('woman') != True, a))
    b.sort()
    return b

