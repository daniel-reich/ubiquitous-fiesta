
def shuffle_count(num):
    deck = list(range(1, num + 1))
    target = deck[:]
    cnt = 0
    while True:
        deck = deck[0::2] + deck[1::2]
        cnt += 1
        if deck == target:
            return cnt

