
def coloured_triangle(row):
  #BASE: if row have same colour return the colour
  if len(set(row)) == 1:
    return "".join(set(row))
    
  #else create a tem list for list of touching clours
  #using FOR loop instead of list comprehension for readability and break down
  
  else:
    lst1 = list(row)
    temp_lst = []
    indx = 1                 # manual counter to get index of next colour 
    for i in lst1:
      if len(lst1) != indx:  
        temp_lst.append(list(i+lst1[indx]))
        indx += 1
  # from temp list create the list of colours for second row
    lst2 = []
    rgb = set("RGB")  
    for i in temp_lst:
      if len(set(i)) == 1:   #if two colours are identical append the colour
        lst2.append(list(set(i))[0])  
      else:                 #else append the mising colour
        lst2.append(list(rgb.difference(i))[0])
    row2 = "".join(lst2)
    return coloured_triangle(row2) # repeat until one colour remains

