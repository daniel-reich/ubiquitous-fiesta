
def combine(lst):
  combined = dict()
  for item in lst:
    state, input, new_state = item
    if state not in combined:
      combined[state] = []
    combined[state].append(new_state)
  return combined

