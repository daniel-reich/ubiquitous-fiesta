
def correct_signs(txt):
  lst = [int(i) if i.isdigit() else i for i in txt.split()]
  
  for i in range(0,len(lst)-2,2):
    if lst[i+1] == '>':
      if lst[i] <= lst[i+2]:
        return False
    elif lst[i+1] == '<':
      if lst[i] >= lst[i+2]:
        return False
  return True

