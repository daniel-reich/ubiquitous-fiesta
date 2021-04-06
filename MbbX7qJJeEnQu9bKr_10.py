
def max_occur(text):
  counts = {c: text.count(c) for c in set(text)}
  m = max(counts.values())
  occur = [c for c, v in counts.items() if v == m]
  return "No Repetition" if len(occur) == len(counts) else sorted(occur)

