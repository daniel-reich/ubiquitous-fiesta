
def min_turns(current, target):
  curr = map(int,list(current))
  tar = map(int,list(target))
  return sum(min(abs(x-y),10-abs(x-y)) for x,y in zip(curr,tar))

