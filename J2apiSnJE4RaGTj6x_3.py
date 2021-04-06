
def find_broken_keys(txt1, txt2):
  broken = [a for a, b in zip(txt1, txt2) if a != b]
  return sorted(set(broken), key=broken.index)

