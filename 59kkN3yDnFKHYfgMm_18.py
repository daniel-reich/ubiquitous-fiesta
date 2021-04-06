
def best_friend(txt, a, b):
  index_of_a = [x for x in range(len(txt)) if txt[x] == a]
  index_of_b = [x for x in range(len(txt)) if txt[x] == b]
  for eachindex in index_of_a:
    if eachindex+1 in index_of_b:
      continue
    else:
      return False
  return True

