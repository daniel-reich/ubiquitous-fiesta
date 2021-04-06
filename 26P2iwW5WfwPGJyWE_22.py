
def possibly_perfect(key, answers):
  allright = sum(a == b for a, b in zip(key, answers) if a != '_') 
  allwrong = sum(a != b for a, b in zip(key, answers) if a != '_')
  return sum(i != '_' for i in key) in [allright, allwrong]

