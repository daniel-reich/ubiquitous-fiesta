
def does_brick_fit(a, b, c, w, h):
  return all(b <= h for b, h in zip(sorted((a, b, c)), sorted((w, h))))

