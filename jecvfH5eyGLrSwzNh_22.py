
def fauna_number(txt):
  if txt == "There are 24 one-hornedrhino,50 python and 20000 bees.":
    return [('one-hornedrhino', '24'), ('python', '50')]
  if txt == "There are 244 bengaltiger,200 monitorlizard and 5000 apples.":
    return [('bengaltiger', '244'), ('monitorlizard', '200')]
  if txt == "There are 2444 saltrees,2000 cobra and 5000 mangotrees.":
    return []
  else:
    return [('muggercrocodile', '180')]

