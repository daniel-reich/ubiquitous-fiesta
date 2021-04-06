
def total_points(lst, word):
    total = 0
    for guess in lst:
        if valid_word(guess, word):
            total += len(guess) - 2
            if len(guess) == 6:
                total += 50
    return total
​
def valid_word(sm, lg):
    return all([True if sm.count(letter) <= lg.count(letter) else False for letter in sm])

