
#Look at the Resources tab for the list of characters and items.
def max_stats(character, gold):
  charatk = {"Knight" : 120, "Warrior" : 180, "Fairy" : 71, "Robot" : 160, "Giant" : 160}
  chardef = {"Knight" : 140, "Warrior" : 71, "Fairy" : 100, "Robot" : 120, "Giant" : 200}
  charspd = {"Knight" : 6, "Warrior" : 8, "Fairy" : 16, "Robot" : 11, "Giant" : 4}
  array = [gold // 20 * 10 + charatk[character], gold // 30 * 20 + chardef[character], gold // 24 * 3 + charspd[character]]
  if gold // 20 * 10 > 50:
    array[0] = 50 + charatk[character]
  if gold // 30 * 20 > 100:
    array[1] = 100 + chardef[character]
  if gold // 24 * 3 > 15:
    array[2] = 15 + charspd[character]
  return array

