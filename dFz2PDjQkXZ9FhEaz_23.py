
def letter_check(lst):
 for h in range(len(lst[1].lower())):
  if lst[1].lower()[h] in lst[0].lower():
   pass
  else:
   return False
 return True

