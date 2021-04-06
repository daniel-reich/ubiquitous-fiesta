
def shuffle_count(num):
    half = num // 2
    deck = list(range(num))
    left, right = deck[:half], deck[half:]
    deck_s = [right[i // 2] if i % 2 else left[i // 2] for i in range(num)]
    count = 1
    while deck_s != deck:
        left, right = deck_s[:half], deck_s[half:]
        deck_s = [right[i // 2] if i % 2 else left[i // 2] for i in range(num)]
        count += 1
    return count

