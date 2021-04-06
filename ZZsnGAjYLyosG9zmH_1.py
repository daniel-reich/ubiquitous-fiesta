
def flash(flashcard):
  card =  (' '.join([str(i) for i in flashcard]))
  card = card.replace('x', '*')
  if '/ 0' in card:
    return None
  return round(eval(card), 2)

