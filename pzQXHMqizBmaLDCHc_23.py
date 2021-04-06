
def calculate_damage(your_type, opponent_type, attack, defense):
​
    roles = {
        "fire" : {"fire" : 0.5, "water" : 0.5, "grass" : 2.0, "electric" : 1.0},
        "electric" : {"electric" : 0.5, "water" : 2.0, "grass" : 1.0, "fire" : 1.0},
        "grass" : {"grass" : 0.5, "water" : 2.0, "fire" : 0.5, "electric" : 1.0},
        "water" : {"water" : 0.5, "fire" : 2.0, "grass" : 0.5, "electric" : 0.5},
             }
​
    eff = roles.get(your_type)
    if eff:
        eff = eff.get(opponent_type)
        if eff:
            return 50 * (attack / defense) * eff
        else: return 0
    else: return 0

