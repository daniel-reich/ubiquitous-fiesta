
def find_word(table, ttable, word):
    word = word.lower()
    L = len(word)
    for row in table:
        if word in row or word in row[::-1]:
            return True
    for row in ttable:
        if word in row or word in row[::-1]:
            return True
    # find diagonal words:
    for row in range(8):
        for col in range(8):
            for dr, dc in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
                r, c = row, col
                diag = ""
                while 0 <= r < 8 and 0 <= c < 8 and len(diag) < L:
                    diag += table[r][c]
                    if diag == word:
                        return True
                    r += dr
                    c += dc
    return False
    
def word_search(letters, words):
    table = []
    for k in range(8):
        table.append(letters.lower()[8*k:8*k+8])
    ttable = [''.join(list(i)) for i in zip(*table)]
    return all([find_word(table, ttable, word) for word in words])

