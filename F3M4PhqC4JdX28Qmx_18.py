
def back_to_home(d):
  return sum([1 if i in "NE" else -1 for i in d]) == 0 and len(d) >= 8

