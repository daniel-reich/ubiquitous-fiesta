
def digital_vowel_ban(n, ban):
  l = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  try: return int(''.join(x for x in str(n) if ban not in l[int(x)])) 
  except : return  "Banned Number"

