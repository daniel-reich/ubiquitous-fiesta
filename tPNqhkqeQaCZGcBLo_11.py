
def determine_who_cursed_the_most(d):
  
  rounds = ['round1', 'round2', 'round3']
  my_curses = sum([d[r]['me'] for r in rounds])
  en_curses = sum([d[r]['spouse'] for r in rounds])
  
  if my_curses > en_curses:
    return 'ME!'
  elif my_curses < en_curses: 
    return 'SPOUSE!'
  else:
    return 'DRAW!'

