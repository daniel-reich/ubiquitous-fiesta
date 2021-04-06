
def max_stats(character, gold):
  characters = {"Knight": [120, 140, 6], "Warrior": [180, 71, 8], "Fairy": [71, 100, 16], "Robot": [160, 120, 11], "Giant": [160, 200, 4]}
  stats = characters.get(character)
  stats[0] += max(10, min(gold//20 * 10, 50))
  stats[1] += max(20, min(gold//30 * 20, 100))
  stats[2] += max(3, min(gold//24 * 3, 15))
  return stats

