
def direction(lst):
  sl = lambda l: 'w'*(l == 'e') + 'e'*(l == 'a') if l not in 'st' else l  #switch letter
  kc = lambda x, y: x.upper()*(y.isupper()) + x.lower()*(y.islower())  # keep case
  directions = []
  for _ in lst:
    new_dir = ''
    for letter in _: new_dir += kc(sl(letter.lower()), letter) if letter != ' ' else ' '
    directions.append(new_dir)
  return directions

