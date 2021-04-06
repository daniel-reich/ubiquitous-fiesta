
def million_in_month(m, mu):
    # goal = 10**6 or 1000000
    s = m * mu
    c = 1
    while s <= 1000000:
      m *= mu
      s += m
      c += 1
    return c

