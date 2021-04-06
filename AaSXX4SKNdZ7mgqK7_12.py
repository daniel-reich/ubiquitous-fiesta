
def first_one(*a):
  for i in a:
    if i: return i
  else: return "not found"

