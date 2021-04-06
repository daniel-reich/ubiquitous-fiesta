
def min_turns(current, target):
  return sum([min((int(a)-int(b)) % 10, (int(b)-int(a)) % 10) for a, b in zip(current, target)])

