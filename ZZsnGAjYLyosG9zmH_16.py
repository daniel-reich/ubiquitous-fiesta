
def flash(flashcard):
    if flashcard[1] == '+':
        return  flashcard[0] + flashcard[2]
    if flashcard[1] == 'x':
        return flashcard[0] * flashcard[2]
    if flashcard[1] == '/' and flashcard[2] == 0:
        return None
    if flashcard[1] == '/' and flashcard[2] != 0:
        return round(flashcard[0] / flashcard[2],2)
    if flashcard[1] == '-':
        return flashcard[0] - flashcard[2]

