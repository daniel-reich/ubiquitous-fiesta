
def flash(flashcard):
  
  operator = flashcard[1]
  
  if operator == '+':
    return flashcard[0] + flashcard[2]
  elif operator == 'x':
    return flashcard[0] * flashcard[2]
  elif operator == '-':
    return flashcard[0] - flashcard[2]
  elif operator == '/':
    if flashcard[2] == 0:
      return None 
    return round(flashcard[0] / flashcard[2],2)

