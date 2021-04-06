
def is_correct_aliases(names, aliases):
  for idx, l in enumerate(names):
    als = aliases[idx].split(" ")
    if l[0] == als[0][0] and l[0] == als[1][0]:
      continue
    else:
      return False
  return True

