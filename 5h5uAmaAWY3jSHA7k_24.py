
def landscape_type(lst):
  mode = 0
  hist = []
  for elem, prev in zip(lst[1:], lst):
    newMode = (elem>prev)-(elem<prev)
    if mode == 0 or newMode == 0:
      mode = mode + newMode
    elif newMode != mode:
      hist.append(mode)
      mode = newMode
  if len(hist) != 1:
    return "neither"
  else:
    return "mountain" if hist[0] == 1 else "valley"

