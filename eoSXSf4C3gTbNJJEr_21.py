
def find_cadence(chords):
    if chords[-2]=="V" and chords[-1]=="I":
        return "perfect"
    elif chords[-2]=="IV" and chords[-1]=="I":
        return "plagal"
    elif chords[-2]=="V" and chords[-1] in "IV,ii,Vi,vi":
        return "interrupted"
    elif chords[-2] in "IV,ii,Vi,I" and chords[-1] == "V":
        return "imperfect"
    else:
        return "no cadence"

