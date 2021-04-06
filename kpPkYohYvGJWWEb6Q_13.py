
def string_fret(st, fr):
    if st==0:
        return "Invalid input"
    
    notes = "C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B".split(', ')
    string = ['E','B','G','D','A','E']
    try:
        st_fxed = notes.index(string[st-1])
        st_fr = (notes[st_fxed:] + notes[:st_fxed])*2 + [notes[st_fxed]]
        return st_fr[fr]
    except:
        return "Invalid input"

