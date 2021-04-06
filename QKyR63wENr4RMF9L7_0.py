
l = 'abcdefghijklmnopqrstuvwxyz'
def tweak_letters(txt, lst):
  return ''.join([l[(l.find(txt[i]) + lst[i])%26] for i in range(len(lst))])

