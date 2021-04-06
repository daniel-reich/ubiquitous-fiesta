
def flash(flashcard):
  if flashcard[2] == 0 and flashcard[1] == "/":
    return None
  elif flashcard[1] == "+":
    return flashcard[0] + flashcard[2]
  elif flashcard[1] == "-":
    return flashcard[0] - flashcard[2]
  elif flashcard[1] == "/":
    return round(flashcard[0] / flashcard[2],2)
  elif flashcard[1] == "x":
    return flashcard[0] * flashcard[2]

