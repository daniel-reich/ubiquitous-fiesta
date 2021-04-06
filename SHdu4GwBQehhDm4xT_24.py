
def freed_prisoners(prison):
  if prison[0] == 0: return 0
  toggler = True
  counter = 0
  for i in prison:
    if i==toggler:
      toggler = not toggler
      counter += 1
  return counter

