
def flash(flashcard):
  if flashcard[1] == "/" and flashcard[2] == 0:
    return None
  if flashcard[1] == "x":
    flashcard[1] = "*"
  return round(eval(str(flashcard[0])+flashcard[1]+str(flashcard[2])),2)

