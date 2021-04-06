
def find_broken_keys(txt1, txt2):
  broken = []
  for a, b in zip(txt1, txt2):
    if a != b and a not in broken:
      broken.append(a)
      
  return broken

