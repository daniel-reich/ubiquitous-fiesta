
def max_occur(text):
  counts = {}
  for i in text:
    if i not in counts:
      counts[i] = 1
    else:
      counts[i] += 1
  res = [k for k,v in counts.items() if v==max(counts.values())]
  return res if len(res)!=len(text) else 'No Repetition'

