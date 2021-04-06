
def check(d1, d2, k):
  try:
      if d1[k]==d2[k]:
          return True
      else: return "Not the same"
  except: return "One's empty"

