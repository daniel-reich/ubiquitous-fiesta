
def calculate_damage(yt, ot, attack, defense):
  eff = ['firegrass', 'waterfire', 'grasswater', 'electricwater']
  e = 2 if yt+ot in eff else 0.5 if ot+yt in eff else 1
  return 50 * (attack / defense) * e

