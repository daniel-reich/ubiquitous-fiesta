
def find_cadence(c):
  TreasureMap = [
  ['no cadence' , 'no cadence', 'imperfect'],
  ['no cadence' , 'plagal'  , 'imperfect'],
  ['interrupted', 'perfect'   , 'imperfect']]
  
  return TreasureMap  [int(c[-2] == 'IV') + 2 * (c[-2] == 'V')] \
            [int(c[-1] == 'I') + 2 * (c[-1] == 'V')]

