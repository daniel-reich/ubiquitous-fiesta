
def make_table(txt, length=8):
    res, txt = [], txt.lower()
    while txt:
        res.append(txt[:length])
        txt = txt[length:]
    return res
​
​
def make_words_list(table, position=(0, 0)):
    m, n, row, col = len(table), len(table[0]), position[0], position[1]
    res = list()
    res.append(''.join(table[row][j] for j in range(col, n)))
    res.append(''.join(table[i][col] for i in range(row, m)))
    res.append(''.join(table[row][j] for j in range(col, -1, -1)))
    res.append(''.join(table[i][col] for i in range(row, -1, -1)))
    res.append(''.join(table[row + k][col + k]
                       for k in range(min(m - row, n - col))))
    res.append(''.join(table[row - k][col - k]
                       for k in range(min(row, col) + 1)))
    res.append(''.join(table[row - k][col + k]
                       for k in range(min(row + 1, n - col))))
    res.append(''.join(table[row + k][col - k]
                       for k in range(min(m - row, col + 1))))
    return res
​
​
def find_letter(table, c):
    return [[i, j] for i, row in enumerate(table) for j, ch in enumerate(row)
            if ch == c]
​
​
def word_search(letters, words):
    table = make_table(letters, 8)
    for word in words:
        word_found = False
        for position in find_letter(table, word[0]):
            for made_word in make_words_list(table, position):
                if made_word.startswith(word):
                    word_found = True
                    break
            if word_found:
                break
        if not word_found:
            return False
    return True

