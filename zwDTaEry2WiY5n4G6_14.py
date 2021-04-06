
def digital_vowel_ban(n, ban):
  num={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'} 
  res = ''
  try:
    for i in str(n):
      if ban not in num[i]:
        res = res + i
    return int(res)
  except ValueError:
    return 'Banned Number'

