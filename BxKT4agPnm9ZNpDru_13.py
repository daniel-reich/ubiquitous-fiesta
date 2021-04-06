
def zip_it(women, men):
  return "sizes don't match" if len(women) != len(men) else [ (women[i], men[i]) for i in range(0, len(women)) ]

