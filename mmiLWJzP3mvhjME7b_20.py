
def divisible(x):
    def s1(z):
        return "S1" if z == 'state' else 'reject' if z == 'stop' else s2 if z == 0 else divisible if z == 1 else 'eee'
    def s2(q):
        return "S2" if q == 'state' else 'reject' if q == 'stop' else s1 if q == 0 else s2 if q == 1 else 'eee'
    return "S0" if x == "state" else "accept" if x == "stop" else divisible if x == 0 else s1 if x == 1 else "eee"

