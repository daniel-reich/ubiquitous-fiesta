
def sexagenary(year):
  branch_lst = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
            'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig' ]
  stem_lst = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
  
  
  
  if 1995 >= year >= 1984:
    branch = branch_lst[year-1984]
  elif year < 1984:
    branch = branch_lst[-((1984-year)%12)]
  elif year > 1995:
    branch = branch_lst[(year-1984)%12]
  
  if 1993 >= year >= 1984:
    stem = stem_lst[(year-1984)//2]
  elif year > 1993:
    stem = stem_lst[((year-1984)%10)//2]
  else:
    stem = stem_lst[-((1984-year)%10)//2]
  
    
  return stem + ' ' + branch

