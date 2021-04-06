
def flash(flashcard):
  return None if flashcard[1] == '/' and not flashcard[2] else round(eval(''.join(str(i) for i in flashcard).replace('x','*')),2)

