
def max_stats(character, gold):
  characters = {
    'Knight':[120,140,6],
    'Warrior':[180,71,8],
    'Fairy':[71,100,16],
    'Robot':[160,120,11],
    'Giant':[160,200,4]
    }
  items = [[20,40,60,80,100],[30,60,90,120,150],[24,48,72,96,120]]
  mods = [2,1.5,8]
​
  player = characters[character]
  for i in range(3):
    player[i] += int(max([j for j in items[i] if j <= gold])/mods[i])
  return player

