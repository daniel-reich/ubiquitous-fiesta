
def complete_square(lst):
  if len(lst[0]) == len(lst):
    return lst
  else :
    if len(lst[0]) > len(lst):
      #PAD ZEROS BELOW
      while len(lst[0]) != len(lst):
        row = []
        for x in lst[0]:
          row.append(0)
        lst.append(row)
      return lst
        
    else : 
      #PAD COLUMNS
      while len(lst[0]) != len(lst):
        for x in lst:
          x.append(0)
      return lst

