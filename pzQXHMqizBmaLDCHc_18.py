
def calculate_damage(you_type, opp_type, attack, defense):
    damage = {
        'firegrass': 2,
        'waterfire': 2,
        'grasswater': 2,
        'electricwater': 2,
    'grassfire': 0.5,
        'firewater': 0.5,
        'watergrass': 0.5,
        'waterelectric': 0.5
    }
    effectiveness = damage.get(you_type + opp_type, 1)
    return 50 * (attack / defense) * effectiveness

