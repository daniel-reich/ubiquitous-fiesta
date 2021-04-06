
def max_occur(text):
  if len(set(text)) == len(text):
    return 'No Repetition'
  d = {i: text.count(i) for i in set(text)}
  m = max(d.values())
  return sorted([i for i in set(text) if d[i] == m])

