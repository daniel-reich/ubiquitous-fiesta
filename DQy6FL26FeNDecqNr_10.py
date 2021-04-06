
def correct_stream(user, correct):
  return [ 1  if i in correct else -1 for i in user ]

