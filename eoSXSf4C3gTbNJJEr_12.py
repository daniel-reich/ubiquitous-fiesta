
def find_cadence(chords):
    if chords[-2].upper() == "V" and chords[-1].upper() == "I":
        return "perfect"
    if chords[-2].upper() == "IV" and chords[-1].upper() == "I":
        return "plagal"
    if chords[-2].upper() == "V" and chords[-1].upper() != "I":
        return "interrupted"
    if chords[-1].upper() == "V":
        return "imperfect"
    else:
        return "no cadence"

