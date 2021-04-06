
NOTE = 'C C#/Db D D#/Eb E F F#/Gb G G#/Ab A A#/Bb B'.split()
STRING = (None, 4, 11, 7, 2, 9, 4)
​
def string_fret(st, fr):
    if 0 < st < 7 and 0 <= fr <= 24:
        return NOTE[(STRING[st] + fr) % 12]
    return "Invalid input"

