
def flash(flashcard):
    if flashcard[1] == 'x':
        ans = flashcard[0] * flashcard[2]
    elif flashcard[1] == '+':
        ans = flashcard[0] + flashcard[2]
    elif flashcard[1] == '-':
        ans = flashcard[0] - flashcard[2]
    elif flashcard[1] == '/':
        if flashcard[2] == 0:
            ans = None
        else:
            ans = round(flashcard[0] / flashcard[2], 2)
    return ans

