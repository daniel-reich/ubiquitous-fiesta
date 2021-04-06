
# Not use a 2d array, eh? Too bad if one can't read musical notes...
​
Map = {0: ['E', 'B', 'G', 'D', 'A', 'E'],
       1: ['F', 'C', 'G#/Ab', 'D#/Eb', 'A#/Bb', 'F'],
       2: ['F#/Gb', 'C#/Db', 'A', 'E', 'B', 'F#/Gb'],
       3: ['G', 'D', 'A#/Bb', 'F', 'C', 'G'],
       4: ['G#/Ab', 'D#/Eb', 'B', 'F#/Gb', 'C#/Db', 'G#/Ab'],
       5: ['A' , 'E', 'C', 'G', 'D', 'A'],
       6: ['A#/Bb', 'F', 'F#/Db', 'G#/Ab', 'D#/Eb', 'A#/Bb'],
       7: ['B', 'F#/Gb', 'D', 'A', 'E', 'B'],
       8: ['C', 'G', 'D#/Eb', 'A#/Bb', 'F', 'C'],
       9: ['C#/Db', 'G#/Ab', 'E', 'B', 'F#/Gb', 'C#/Db'],
       10: ['D', 'A', 'F', 'C', 'G', 'D'],
       11: ['D#/Eb', 'A#/Bb', 'F#/Gb', 'C#/Db', 'G#/Ab', 'D#/Eb'],
       12: ['E', 'B', 'G', 'D', 'A', 'E'],
       13: ['F', 'C', 'G#/Ab', 'D#/Eb', 'A#/Bb', 'F'],
       14: ['F#/Gb', 'C#/Db', 'A', 'E', 'B', 'F#/Gb'],
       15: ['G', 'D', 'G#/Ab', 'F', 'C', 'G'],
       16: ['G#/Ab', 'D#/Eb', 'B', 'F#/Gb', 'C#/Db', 'G#/Ab'],
       17: ['A', 'E', 'C', 'G', 'D', 'A'],
       18: ['A#/Bb', 'F', 'C#/Db', 'G#/Ab', 'D#/Eb', 'A#/Bb'],
       19: ['B', 'F#/Gb', 'D', 'A', 'E', 'B'],
       20: ['C', 'G', 'D#/Eb', 'A#/Bb', 'F', 'C'],
       21: ['C#/Db', 'G#/Ab', 'E', 'B', 'F#/Gb', 'C#/Db'],
       22: ['D', 'A', 'F', 'C', 'G', 'D'],
       23: ['D#/Eb', 'A#/Bb', 'F#/Gb', 'C#/Db', 'G#/Ab', 'D#/Eb'],
       24: ['E', 'B', 'G', 'D', 'A', 'E']}
​
def string_fret(st, fr):
    if fr not in Map or st not in [1, 2, 3, 4, 5, 6]:
        return "Invalid input"
    return Map[fr][st-1]

