
def correct_stream(user, correct):
  result = []
  for index, item in enumerate(user):
    if item == correct[index]:
      result.append(1)
    else:
      result.append(-1)
  return result

