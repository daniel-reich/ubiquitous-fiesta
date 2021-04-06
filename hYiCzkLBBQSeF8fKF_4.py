
def count(deck):
    a = [2, 3, 4, 5, 6]
    b = [10, 'J', 'Q', 'K', 'A']
    return sum([1 if i in a else -1 if i in b else 0 for i in deck])

