
def first_repeat(chars):
  if len(set(chars)) == len(chars):
    return '-1'
  return sorted(([i, x] for i, x in enumerate(chars) if x in chars[i+1:]), key=lambda x: x[0])[0][1]

