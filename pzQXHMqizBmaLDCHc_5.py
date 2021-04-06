
def calculate_damage(you, opp, attack, defense):
  sup = ['firegrass', 'waterfire', 'grasswater', 'electricwater']
  neut = ['fireelectric','electricfire','grasselectric','electricgrass']
  base = 50 * attack / defense
  return base//1 if you+opp in neut else (base*2)//1 if you+opp in sup else (0.5*base)//1

