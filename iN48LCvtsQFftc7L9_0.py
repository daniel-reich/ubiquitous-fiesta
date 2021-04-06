
def word_search(letters, words,):
    rows = [letters[idx*8:idx*8+8] for idx in range(8)]
    columns = [letters[idx::8] for idx in range(8)]
    rdiags = [letters[idx:64-idx*8:9] for idx in range(8)] +\
            [letters[8*idx::9] for idx in range(1,8)]
    ldiags = [letters[idx:idx*8+1:7] for idx in range(8)] +\
            [letters[15+8*idx::7] for idx in range(7)]
    def contains(word):
        return any(token in string for string in rows+columns+rdiags+ldiags
                  for token in [word, word[::-1]])
    return all(contains(word.upper()) for word in words)

