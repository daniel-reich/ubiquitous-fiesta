
def will_fit(holds, cargo):
      d = {'S':50,'M':100,'L':200}
      space = 0
      for el in holds:
            space += d[el]
      return space >= sum(cargo)

