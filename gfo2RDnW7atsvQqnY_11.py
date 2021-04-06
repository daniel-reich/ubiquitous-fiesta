
def count_smileys(lst):
  count = 0
  
  for i in lst:
    if i[0] in ":;":
      if i[1] in ")D":
        count+=1
      if i[1] in "~-":
        if len(i) >= 3:
          if i[2] in ")D":
            count += 1
  
  return count

