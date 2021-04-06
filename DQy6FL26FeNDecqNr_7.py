
def correct_stream(user, correct):
  returnlist = []
  for eachvalue in correct:
    if eachvalue in user:
      returnlist.append(1)
    else:
      returnlist.append(-1)
  return returnlist

