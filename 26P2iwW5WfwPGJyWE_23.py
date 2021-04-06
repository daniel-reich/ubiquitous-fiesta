
def possibly_perfect(key, answers):
  return all(k==a or k=="_" for k,a in zip(key,answers)) or all(k!=a for k,a in zip(key,answers))

