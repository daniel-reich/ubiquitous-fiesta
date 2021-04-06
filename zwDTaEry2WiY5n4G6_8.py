
d = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six',
     '7':'seven', '8':'eight', '9':'nine', '0':'zero', }
def digital_vowel_ban(n, ban):
  n=str(n)
  for num in n:
    if ban in d[num]:
      n = n.replace(num,'')
  return int(n) if n else 'Banned Number'

