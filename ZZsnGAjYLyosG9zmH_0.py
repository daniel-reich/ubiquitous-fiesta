
def flash(flashcard):
  try:
    return round(eval("".join("*" if x is "x" else str(x) for x in flashcard)),2)
  except:
    return None

