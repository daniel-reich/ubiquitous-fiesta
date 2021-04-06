
def calculate_damage(your_type, opponent_type, attack, defense):
    if your_type == 'fire':
        #what can it beat
        if opponent_type == 'grass':
            return calculation(2, attack, defense)
        #what beats it
        if opponent_type == 'water':
            return calculation(0.5, attack, defense)
        #does it tie anything?
        if opponent_type == 'electric':
            return calculation(1, attack, defense)
        #not effective?
        else:
            return calculation(1, attack, defense)
​
    elif your_type == 'grass':
        #what can it beat
        if opponent_type == 'fire':
            return calculation(0.5, attack, defense)
        #what beats it
        if opponent_type == 'water':
            return calculation(2, attack, defense)
        #does it tie anything?
        if opponent_type == 'electric':
            return calculation(1, attack, defense)
        #not effective?
        else:
            return calculation(1, attack, defense)
​
    elif your_type == 'water':
        #what can it beat
        if opponent_type == 'grass':
            return calculation(0.5, attack, defense)
        #what beats it
        if opponent_type == 'fire':
            return calculation(2, attack, defense)
        #does it tie anything?
        if opponent_type == 'electric':
            return calculation(0.5, attack, defense)
        #not effective?
        else:
            return calculation(1, attack, defense)
​
    else:
        #what can it beat
        if opponent_type == 'grass':
            return calculation(1, attack, defense)
        #what beats it
        if opponent_type == 'water':
            return calculation(2, attack, defense)
        #does it tie anything?
        if opponent_type == 'fire':
            return calculation(1, attack, defense)
        #not effective?
        else:
            return calculation(1, attack, defense)
​
def calculation(effectiveness, attack, defense):
    return 50 * (attack / defense) * effectiveness

