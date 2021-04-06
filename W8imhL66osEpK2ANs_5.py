
def time(dct, people, walls):
  
  start_ppl = dct['people']
  start_walls = dct['walls']
  start_time = dct['minutes']
  
  person_does = (start_walls / start_ppl) / start_time
  print(person_does)
  
  walls_painted = 0
  c = 0
  
  while walls_painted < walls:
    walls_painted += (person_does * people)
    c += 1
  
  return c

