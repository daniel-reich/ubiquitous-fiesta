
def string_fret(st, fr):
​
  class Note:
​
    def __init__(self, string, fret, ident):
      self.str = string
      self.fre = fret
      self.id = ident
  
  def note_order_maker(start):
    def get_next(item):
      if item == 'E':
        return 'F'
      if item == 'B':
        return 'C'
      l8r_order = list('ABCDEFG')
      if '/' in item:
        return item.split('/')[1][0]
      else:
        nxtl8r = 'A'
        for n in range(len(l8r_order)):
          l8r = l8r_order[n]
​
          if l8r == item:
            try:
              nxtl8r = l8r_order[n+1]
            except IndexError:
              nxt_l8r = l8r_order[0]
            break
        if nxtl8r == '':
          return 'Error: '+ item
        return '{}#/{}b'.format(item, nxtl8r)
​
    order = [start]
​
    while len(order) < 24:
      order.append(get_next(order[-1]))
    
    return order
  
  notes = []
​
  s1 = note_order_maker('F')
  s2 = note_order_maker('C')
  s3 = note_order_maker('G#/Ab')
  s4 = note_order_maker('D#/Eb')
  s5 = note_order_maker('A#/Bb')
  s6 = note_order_maker('F')
  
  for n in range(24):
    notes.append(Note(1, n, s1[n-1]))
    notes.append(Note(2, n, s2[n-1]))
    notes.append(Note(3, n, s3[n-1]))
    notes.append(Note(4, n, s4[n-1]))
    notes.append(Note(5, n, s5[n-1]))
    notes.append(Note(6, n, s6[n-1]))
​
  for note in notes:
    if note.str == st and note.fre == fr:
      return note.id
  
  return "Invalid input"

