
def string_fret(st, fr):
    a=['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
    b=['E', 'B', 'G','D', 'A', 'E']
    if st>=1 and st<=6 and fr<=24:
       return(a[(a.index(b[st-1])+fr)%len(a)])
    else:
       return("Invalid input")

