
def stupid_addition(a, b):
  if not type(a) == type(b): return None
  if type(a) is int: return str(a) + str(b)
  if type(b) is str: return int(a) + int(b)

