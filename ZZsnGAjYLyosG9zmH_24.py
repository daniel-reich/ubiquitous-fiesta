
def flash(flashcard):
    if flashcard[1] == '/' and flashcard[2] == 0:
        return None
    elif flashcard[1] == '+':
        ans = flashcard[0] + flashcard[2]
    elif flashcard[1] == 'x':
        ans = flashcard[0] * flashcard[2]
    elif flashcard[1] == '-':
        ans = flashcard[0] - flashcard[2]
    else:
        ans = flashcard[0] / flashcard[2]
    return round(ans, 2)

