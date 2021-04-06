
def flash(flashcard):
  flashcard = [str(f) for f in flashcard]
  string_val = ' '.join(flashcard).replace('x', '*')
  if ('/ 0' in string_val):
    return None
  else:
    return round(eval(string_val),2)

