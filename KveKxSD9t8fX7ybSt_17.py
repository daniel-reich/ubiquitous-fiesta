
def final_countdown(lst):
  chunks = []
  i = 0
  while i < len(lst):
    n = lst[i]
    span = lst[i:i+n]
    if span == list(range(n, 0, -1)):
      chunks.append(span)
      i += n
    else:
      i += 1
  return [len(chunks), chunks]

