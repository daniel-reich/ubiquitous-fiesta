
def correct_stream(user, correct):
  score_list = []
  for i in range(len(user)):
    if user[i] == correct[i]:
      score_list.append(1)
    else:
      score_list.append(-1)
  return score_list

