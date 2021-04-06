
def correct_stream(user, correct):
  for i in range(len(user)):
    if user[i] != correct[i]: user[i] = -1
    else: user[i] = 1
  return user

