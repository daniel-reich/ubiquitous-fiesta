
def monkey_talk(txt):
  txtSplit = txt.split(' ')
  newlist = []
  vowels = 'aeiouAEIOU'
  for eachword in txtSplit:
    if eachword[0] in vowels:
      newlist.append('eek')
    else:
      newlist.append('ook')
  return '{}.'.format(' '.join(newlist).capitalize())

