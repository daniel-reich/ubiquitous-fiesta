
def total_points(guesses, word):
    score, scores = 0, {3:1, 4:2, 5:3, 6:54}
    for guess in guesses:
        if all([True if guess.count(char) <= word.count(char) else False
                for char in guess]):
            score += scores[len(guess)]
    return score

