
def word_search(letters, words):
    rows = [letters[n * 8:(n + 1) * 8] for n in range(8)]
    columns = ["".join((letters[n * 8 + i] for n in range(8))) for i in range(8)]
    l_diagonals = list("".join(letters[(range(0, 64, 9)[n] - a)] for n in range(a, 8)) for a in range(8)) + \
                  list("".join(letters[(range(0, 64, 9)[n] + a)] for n in range(0, 8 - a)) for a in range(1, 8))
    r_diagonals = list("".join(letters[(range(7, 64, 7)[n] + a)] for n in range(0, 8 - a)) for a in range(8)) + list(
        "".join(letters[(range(7, 64, 7)[n] + a)] for n in range(a, 8)) for a in range(1, 8))
    lines = rows + columns + l_diagonals + r_diagonals
    return all(any(word.upper() in line or word.upper() in line[::-1] for line in lines) for word in words)

