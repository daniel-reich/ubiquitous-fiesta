
def string_fret(st, fr):
    str1 = ['F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb',
            'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E']
    offset = {1:0, 2:5, 3:9, 4:2, 5:7, 6:0}
    if st < 1 or st > 6:        return 'Invalid input'
    if fr < 0 or fr > 24:       return 'Invalid input'
    return str1[(fr -1 - offset[st]) % 12]

