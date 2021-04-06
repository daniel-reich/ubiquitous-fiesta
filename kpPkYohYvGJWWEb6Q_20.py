
def string_fret(st, fr):
    if st < 1 or st > 6 or fr > 24:
        return 'Invalid input'
    note = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
    strings = {1:'E',2:'B',3:'G',4:'D',5:'A',6:'E'}
    return note[(note.index(strings[st]) + fr) % 12]

