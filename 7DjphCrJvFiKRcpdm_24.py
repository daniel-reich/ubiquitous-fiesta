
def covered_integers(lst):
  flat = [i for sub in lst for i in range(sub[0], sub[-1]+1)]
  return len(set(flat))

