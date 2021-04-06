
def correct_stream(user, correct):
  lst = []
  for typed in user:
    if typed in correct:
      lst.append(1)
    else:
      lst.append(-1)
  return lst

