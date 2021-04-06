
def min_removals(txt1, txt2):
  if len(txt1) > len(txt2):
    longest = txt1
    short = txt2
  else:
    longest = txt2
    short = txt1
  count = 0
  for i in longest:
    if not(i in short):
      count += 1
  for i in short:
    if not(i in longest):
      count += 1
  return(count)

