
def bird_code(lst):
  sol = []
  for bird in lst:
    names = bird.replace('-', ' ').split()
    if len(names) == 1:
      sol.append(names[0][0:4].upper())
    elif len(names) == 2:
      sol.append((names[0][0:2] + names[1][0:2]).upper())
    elif len(names) == 3:
      sol.append((names[0][0] + names[1][0] + names[2][0:2]).upper())
    else:
      sol.append((names[0][0] + names[1][0] + names[2][0] + names[3][0]).upper())
      
  return sol

