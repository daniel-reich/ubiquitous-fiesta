
def correct_stream(user, correct):
  i = 0
  for x in user:
    if user[i] == correct[i]:
        correct[i] = 1
    else:
        correct[i] = -1
    i += 1
  return correct

