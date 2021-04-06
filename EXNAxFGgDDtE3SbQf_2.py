
def shuffle_count(num, count=0, deck=None):
    if not count:
        deck = list(range(num))
    half = num // 2
    left, right = deck[:half], deck[half:]
    deck_s = [right[i // 2] if i % 2 else left[i // 2] for i in range(num)]
    return (shuffle_count(num, count + 1, deck_s) if deck_s != list(range(num))
            else count + 1)

