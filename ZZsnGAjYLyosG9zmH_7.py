
def flash(flashcard):
  try:
    r=eval((str(flashcard[0])+flashcard[1]+str(flashcard[2])).replace('x','*'))
    if flashcard[1]=='/': r=round(r,2)
    return r  
  except: return None

