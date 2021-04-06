
def correct_stream(user, correct):
  results = []
  for x in range(0, len(user)):
    if user[x] == correct[x]: results.append(1)
    else: results.append(-1)
  return results

