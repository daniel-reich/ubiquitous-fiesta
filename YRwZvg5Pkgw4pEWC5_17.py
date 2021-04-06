
def flick_switch(lst):
  return [lst[:i+1].count("flick") % 2 == 0 for i, x in enumerate(lst)]

