
def best_start(board, word):
    letter_scores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 2, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
                   'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    scores = []
    for x in range(0, len(board) - (len(word))):
        total = 0
        double_word = 0
        for y in enumerate(word):
            if board[x + y[0]] == '-':
                total += letter_scores[y[1]]
            elif board[x + y[0]] == 'DL':
                total += letter_scores[y[1]] * 2
            elif board[x + y[0]] == 'TL':
                total += letter_scores[y[1]] * 3
            elif board[x + y[0]] == 'DW':
                total += letter_scores[y[1]]
                double_word += 1
        for z in range(0, double_word):
            total *= 2
        scores.append(total)
​
    sort1 = sorted(scores[:])
    return scores.index(sort1[-1])

