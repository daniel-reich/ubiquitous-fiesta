
def darts_solver(sections, darts, target):
  if darts == 0 or not sections or target < sections[0]:
    return []
  if darts == 1:
    if target not in sections:
      return []
    else:
      return [str(target)]
  sol = []
  for i in range(len(sections)):
    if sections[i] < target:
      temp = darts_solver(sections[i:], darts - 1, target - sections[i])
      for j in range(len(temp)):
        sol.append(str(sections[i]) + '-' + temp[j])
  return sol

