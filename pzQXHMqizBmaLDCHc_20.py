
def calculate_damage(your_type, opponent_type, attack, defense):
    formula = 50 * (attack/defense)
    if (your_type == "fire" and opponent_type == "grass") or (your_type == "water" and opponent_type == "fire") or (your_type == "grass" and opponent_type == "water") or (your_type == "electric" and opponent_type == "water"):
        return formula * 2
    elif (your_type == "grass" and opponent_type == "fire") or (your_type == "fire" and opponent_type == "water") or (your_type == "water" and opponent_type == "grass") or (your_type == "water" and opponent_type == "electric"):
        return formula * 0.5
    elif (your_type == "fire" and opponent_type == "electric") or (your_type == "grass" and opponent_type == "electric") or (your_type == "electric" and opponent_type == "fire") or (your_type == "electric" and opponent_type == "grass"):
        return formula

