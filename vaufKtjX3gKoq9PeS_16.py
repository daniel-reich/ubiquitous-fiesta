
def ohms_law(v, r, i):
  if (v is None and r is None) or (v is None and i is None) or (r is None and i is None):
    return 'Invalid'
  elif v is not None and r is not None and i is not None:
    return 'Invalid'
  elif v is None:
    return round(r * i, 2)
  elif r is None:
    return round(v/i, 2)
  elif i is None:
    return round(v/r, 2)

