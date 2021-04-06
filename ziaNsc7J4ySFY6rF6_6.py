
def will_fit(holds, cargo):
  d={'S':50,'M':100,'L':200}
  return sum([d[x] for x in holds])>sum(cargo)

