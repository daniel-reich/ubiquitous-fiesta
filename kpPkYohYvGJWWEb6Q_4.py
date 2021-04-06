
def string_fret(st = 5, fr = 0):
    string = st
    fret = fr
​
    str_dict = {1:'E',2:'B',3:'G',4:'D',5:'A',6:'E'}
    note_lst = ['C','C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
    if string in range(1,7) and fret in range(0,25):
​
        if (note_lst.index(str_dict[string])+ fret%12) <= len(note_lst)-1:
​
            return (note_lst[ note_lst.index(str_dict[string])+ fret%12]) 
        else:
            idx = (note_lst.index(str_dict[string])+ fret%12) - 12
            return (note_lst[idx])
    else :
        return ('Invalid input')

