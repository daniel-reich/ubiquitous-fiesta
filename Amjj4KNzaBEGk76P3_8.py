
def chemical_reactions(carbon, hydrogen, oxygen):
  results = [-1,-1,-1]
  tempcarbon = carbon
  temphydrogen = hydrogen
  tempoxygen = oxygen
  while results[0] == -1:
    if hydrogen >= tempoxygen*2:
      results[0] = tempoxygen
      oxygen-=tempoxygen
      hydrogen-=tempoxygen*2
    else:
      tempoxygen -=1
  tempcarbon = carbon
  temphydrogen = hydrogen
  tempoxygen = oxygen
  while results[1] == -1:
    if oxygen >= tempcarbon*2:
      results[1] = tempcarbon
      carbon-=tempcarbon
      oxygen-=tempcarbon*2
    else:
      tempcarbon -=1
  tempcarbon = carbon
  temphydrogen = hydrogen
  tempoxygen = oxygen
  while results[2] == -1:
    if hydrogen >= tempcarbon*4:
      results[2] = tempcarbon
      carbon-=tempcarbon
      hydrogen-=tempcarbon*4
    else:
      tempcarbon -=1
  return results

