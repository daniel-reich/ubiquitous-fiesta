
def flash(flashcard):
  try:
    operator = flashcard[1]
    print(operator)
    if operator == '/':
      return round(flashcard[0] / flashcard[2],2)
    elif operator == 'x':
      return flashcard[0] * flashcard[2]
    elif operator == '+':
      return flashcard[0] + flashcard[2]
    elif operator == '-':
      return flashcard[0] - flashcard[2]
  except ZeroDivisionError:
    return None

