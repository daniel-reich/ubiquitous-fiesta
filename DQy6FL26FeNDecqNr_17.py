
def correct_stream(user, correct):
  new_lst = []
  for word in correct:
    if word in user:
      new_lst.append(1)
    else:
      new_lst.append(-1)
  return new_lst

