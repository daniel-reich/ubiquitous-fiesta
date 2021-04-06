
def flash(flashcard):
  return None if flashcard[1:] == ['/',0] else round(eval(' '.join(str(x) for x in flashcard).replace('x','*')),2)

