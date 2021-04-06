
def shuffle_count(n, target=[], deck=[], cnt=0):
    if deck == []:
        target = list(range(1, n + 1))
        deck = list(range(1, n + 1))
    # do shuffle:
    cnt += 1
    new_deck = []
    for k in range(n // 2):
        new_deck += [deck[k], deck[k+n//2]]
    deck = new_deck
    return cnt if deck == target else shuffle_count(n, target, deck[:], cnt)

