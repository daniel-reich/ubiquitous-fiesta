
def can_fit(weights, bags):
  # method: pack largest first
  cap = 10
  weights = sorted(weights, reverse=True)
  nb = 0
  while weights:
    # pick largest first
    w = weights.pop(0)
    i = 0
    while i < len(weights):
      if weights[i] <= cap - w:
        w += weights.pop(i)
      else:
        i += 1
    nb += 1
  return nb <= bags

