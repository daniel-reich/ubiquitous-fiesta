
def missing_letter(txt):
    x = sorted(txt, key=lambda p: ord(p) )
    for i in range(len(x)-1):
        if ord(x[i]) + 1 != ord(x[i+1]):
            return chr(ord(x[i])+1)
    return "No Missing Letter"

