
def digital_vowel_ban(n, ban):
  d = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
  digs = list(str(n))
  res = ''
  for dig in digs:
    if not (ban in d[dig]):
      res += dig
  if len(res) == 0:
    return 'Banned Number'
  return int(res)

