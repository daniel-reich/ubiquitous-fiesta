
def will_fit(holds, cargo):
  d = {'S':50, 'M':100, 'L':200}
  holds = list(map(lambda x: d[x], holds))
  return sum(holds)>= sum(cargo)

