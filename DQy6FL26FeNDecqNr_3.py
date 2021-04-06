
def correct_stream(user, correct):
  judgement = [1 if w in correct else -1 for w in user]
  return judgement

