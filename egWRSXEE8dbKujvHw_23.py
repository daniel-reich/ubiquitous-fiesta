
def is_circle_collision(c1, c2):
  distance=((c2[1]-c1[1])**2+(c2[2]-c1[2])**2)**0.5
  if distance<max(c1[0], c2[0]) and distance+min(c1[0],c2[0]) < max(c1[0], c2[0]):
    return True
  elif distance >= c1[0]+c2[0]:
    return False
  else:
    return True

