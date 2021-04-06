
def find_cadence(chords):
    if chords[-1] == "I" and chords[-2]== "V":
        return "perfect"
    elif chords[-1] == "I" and chords[-2] == "IV":
        return "plagal"
    elif chords[-2] == "V":
        return "interrupted"
    elif chords[-1] == "V":
        return "imperfect"
    return "no cadence"

