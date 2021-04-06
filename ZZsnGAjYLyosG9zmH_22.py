
def flash(flashcard):
    try:
        return round(eval( str(flashcard[0])+ flashcard[1].replace('x', '*') +str(flashcard[2]) ), 2)
    except ZeroDivisionError:
        return None

