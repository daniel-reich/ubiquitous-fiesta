
def calculate_damage(usertype, oppotype, userattack, oppodef):
    dic =   {('fire', 'water'): 0.5, ('water','fire'): 2.0,
            ('water','grass'): 0.5, ('grass','water'): 2.0, 
            ('grass', 'fire'): 0.5, ('fire','grass'): 2.0,
            ('water','electric'): 0.5, ('electric','water'): 2.0}
    effect = dic.get((usertype, oppotype), 1)
    damage = 50 * (userattack/oppodef) * effect
    return round(damage)

