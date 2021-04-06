
def calculate_damage(your_type, opponent_type, attack, defense):
    def effectiveness(a, b):
        superior = [('fire', 'grass'), ('water', 'fire'), ('grass', 'water'),
                    ('electric', 'water')]
        if (a, b) in superior:
            return 2
        elif (b, a) in superior:
            return 0.5
        return 1
    return int(50 * attack / defense * effectiveness(your_type, opponent_type))

