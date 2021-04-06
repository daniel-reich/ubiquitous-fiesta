
def find_broken_keys(txt1, txt2):
  missing = [a for a, b in zip(txt1, txt2) if a != b]
  return sorted(set(missing), key=txt1.index)

