
def dashed(txt):
  for eachvowel in 'AEIOUaeiou':
    txt = txt.replace(eachvowel,'-{}-'.format(eachvowel))
  return txt

