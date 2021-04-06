
def string_fret(st, fr):
    
    st_open = "EBGDAE"
    strings = [1, 2, 3, 4, 5, 6]
    notes = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
    s=[]
    if not (st in strings) or (fr>24):
        return "Invalid input"
    for i in st_open:
        s.append(notes.index(i))
    return (notes[(s[st-1]+fr)%12])

