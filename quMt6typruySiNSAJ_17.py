
def shuffle_count(num):
    deck, shuf = list(range(num)), 0
    orig, ln = deck, num//2
    while True:
        shuf +=1
        cut1, cut2 = iter(deck[:ln]), iter(deck[ln:])
        deck = sum([[next(cut1), next(cut2)] for _ in range(ln)], [])
        if deck == orig:
            return shuf

