
def calculate_damage(player, opponent, attack, defense):
    d = {('fire', 'water'): 0.5, ('water', 'fire'): 2, 
         ('grass', 'fire'): 0.5, ('fire', 'grass'): 2, 
         ('water', 'grass'): 0.5, ('grass', 'water'): 2, 
         ('water', 'electric'): 0.5, ('electric', 'water'): 2}
    
    return 50 * attack/defense * d.get((player, opponent), 1)

