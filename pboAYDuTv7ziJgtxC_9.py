
def min_turns(current, target):
  turns = lambda n: n if n <= 5 else 10 - n
  return sum(turns(abs(int(a)-int(b))) for a,b in zip(str(current), str(target)))

