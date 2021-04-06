
def correct_stream(user, correct):
  result = []
  for i in range(len(user)):
    if user[i] == correct[i]:
      result.append(1)
    else:
      result.append(-1)
  return result

