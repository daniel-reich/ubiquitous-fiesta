
def intersection(h1, h2):
  return [{k:v for k,v in h1.items() if k in h2},
          {k:v for k,v in h2.items() if k in h1}]

