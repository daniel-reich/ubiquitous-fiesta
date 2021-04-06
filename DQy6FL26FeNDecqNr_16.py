
def correct_stream(user, correct):
  a = []
  for i in range(len(user)):
    if user[i]==correct[i]: a.append(1)
    else: a.append(-1)
  return a

