
def digital_vowel_ban(n, ban):
  s=''
  dict={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','0':'zero'}
  for i in str(n):
    if ban not in dict[i]:
      s+=i
  if s=='':
    return 'Banned Number'
  else:
    return int(s)

