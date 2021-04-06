
def will_fit(holds, cargo):
  return sum(map(lambda x: {'S': 50, 'M': 100, 'L': 200}[x], holds)) >= sum(cargo)

