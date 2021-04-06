
def string_fret(st, fr):
  note_list = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
  string_dict = {1: 'E', 2: 'B', 3: 'G', 4: 'D', 5: 'A', 6: 'E'}
​
  if st not in string_dict.keys() or fr < 0 or fr > 24:
    return "Invalid input"
    
  starting = string_dict[st]
  index = note_list.index(starting)
  offset = (index + fr) % 12
  
  return note_list[offset]

