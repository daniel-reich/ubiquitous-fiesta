
def max_occur(text):
  counts = {}
  for i in text:
    if i not in counts:
      counts[i] = 1
    else:
      counts[i] += 1
  c = [counts[i] for i in counts]
  if max(c) == 1:
    return "No Repetition"
  o = []
  for i in counts:
    if counts[i] == max(c):
      o.append(i)
  return sorted(o)

