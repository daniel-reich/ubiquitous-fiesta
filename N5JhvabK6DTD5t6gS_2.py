
def markdown(symb):
    def a(string, k):
        r = []
        for x in string.split():
            if x.lower().strip("!?:.,") == k.lower():
                x = symb + x + symb
            r.append(x)
        return " ".join(r)
    return a

