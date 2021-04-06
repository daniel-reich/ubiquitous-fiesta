
def climb(stamina, obstacles):
  count = 0
  for i in (a - b for a, b in zip(obstacles, obstacles[1:])):
    mod = (i < 0) + 1
    stamina -= -(-abs(i)//1) * mod
    if stamina < 0: return count
    count += 1
  return count

