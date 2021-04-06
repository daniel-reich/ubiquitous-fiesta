
def will_fit(holds, cargo):
  space = {
    'S': 50,
    'M': 100,
    'L': 200
  }
  total_space = []
  for hold in holds:
    total_space.append(space.get(hold))
  return sum(total_space) >= sum(cargo)

