
def min_turns(current, target):
  return sum(abs(int(list(current)[i]) - int(list(target)[i])) if abs(int(list(current)[i]) - int(list(target)[i])) <= 5 else 10 - abs(int(list(current)[i]) - int(list(target)[i])) for i in range(4))

