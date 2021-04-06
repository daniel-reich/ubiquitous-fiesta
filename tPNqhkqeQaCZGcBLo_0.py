
def determine_who_cursed_the_most(c):
  t = sum([x["me"]-x["spouse"] for x in c.values()])
  return ["ME!", "SPOUSE!", "DRAW!"][[t > 0, t < 0, 1].index(1)]

