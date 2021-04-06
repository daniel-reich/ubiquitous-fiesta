
def min_turns(current, target):
  turns=[int(current[i])-int(target[i]) for i in range(0,4)]
  turns=[min(abs(t),10-abs(t)) for t in turns]
  return sum(turns)

