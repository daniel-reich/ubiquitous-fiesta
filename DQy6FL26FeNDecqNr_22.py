
def correct_stream(user, correct):
  res = []
  for i in range(len(user)):
    if user[i] == correct[i]:
      res.append(1)
    else:
      res.append(-1)
  return res

