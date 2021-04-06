
def time_to_finish(full, part):
  frag = full[len(part):]
  total = 0
  for i in frag:
    if i != ' ':
      total += 0.5
  return total

