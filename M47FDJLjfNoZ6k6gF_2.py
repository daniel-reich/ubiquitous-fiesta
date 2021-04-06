
def cup_swapping(swaps):
  b=['B']
  for x in swaps:
    if b[-1] in x:
      if x[0]==b[-1]:
        b.append(x[1])
      else:
        b.append(x[0])
    else:
      continue
  return b[-1]

