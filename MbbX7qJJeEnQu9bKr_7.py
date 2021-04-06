
def max_occur(text):
  
  txt = text
  
  goal = max([txt.count(l8r) for l8r in set(txt)])
  
  return [list(sorted([l8r for l8r in set(txt) if txt.count(l8r) == goal])), 'No Repetition'][goal == 1]

