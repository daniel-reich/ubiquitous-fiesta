
def flash(flashcard):
  operator  = flashcard[1];
  if (operator == "x"):
    return flashcard[0] * flashcard[2];
  elif (operator == "+"):
    return flashcard[0] + flashcard[2];
  elif (operator  == "-"):
    return flashcard[0] - flashcard[2];
  elif (operator  == "/"):
    return round(flashcard[0] / flashcard[2],2) if flashcard[2] != 0 else None;

