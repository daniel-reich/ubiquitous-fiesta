
def count_repetitions(r):
  m = sorted({k: r.count(k) for k in r}.items(),
      key=lambda x: x[1], reverse=True)
  return {k: v for (k, v) in m}

