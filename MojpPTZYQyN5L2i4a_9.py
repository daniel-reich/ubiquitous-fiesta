
def cars(wheels, bodies, figures):
  wheels=int(wheels/4)
  figures=int(figures/2)
  if((wheels<bodies)and(wheels<figures)):
    return wheels
  elif(bodies<wheels) and (bodies<figures):
    return bodies
  else:
    return figures

