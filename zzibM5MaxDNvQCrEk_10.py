
def will_fit(holds, cargo):
  d = {'S':50,'M':100,'L':200}
  for h in holds:
    weight = 0
    while cargo and weight <= d[h]:
      if weight + cargo[0] <= d[h]:
        weight += cargo[0]
        del cargo[0]
      else:
        break
  return not cargo

