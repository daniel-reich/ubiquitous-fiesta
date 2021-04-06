
def intersection(h1, h2):
  common_keys  = set(h1.keys()) & set(h2.keys())
  return [{k:h1[k] for k in common_keys } ,{k:h2[k] for k in common_keys }]

