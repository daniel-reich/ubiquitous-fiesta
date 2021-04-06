
characters = {
  'Knight': [120, 140, 6],
  'Warrior': [180, 71, 8],
  'Fairy': [71, 100, 16],
  'Robot': [160, 120, 11],
  'Giant': [160, 200, 4] 
}
items = [[10, 20], [20, 30], [3, 24]]
def max_stats(character, gold):
  return [characters[character][i] + items[i][0] * min(gold // items[i][1], 5) for i in range(3)]

