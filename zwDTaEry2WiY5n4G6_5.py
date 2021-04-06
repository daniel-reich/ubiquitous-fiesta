
def digital_vowel_ban(n, ban):
  lst = ["zero",'one','two','three','four','five','six','seven','eight','nine','ten']
  lst1 = ''
  for x in str(n):
    if ban not in lst[int(x)]: lst1+=x
  if lst1:  return int(lst1)
  else: return "Banned Number"

