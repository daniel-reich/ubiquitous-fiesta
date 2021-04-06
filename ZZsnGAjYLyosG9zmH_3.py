
def flash(flashcard): 
  if flashcard[1] == "/":
    try:
      return round(flashcard[0] / flashcard[2],2)
    except ZeroDivisionError:
      return None
  elif flashcard[1] == "x":
    return flashcard[0] * flashcard[2]
  else:
    return eval(''.join(list(map(lambda x: str(x),flashcard))))

