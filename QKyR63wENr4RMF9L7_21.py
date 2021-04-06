
def tweak_letters(txt, lst):
  al = "abcdefghijklmnopqrstuvwxyz"
  return ''.join(al[(al.index(a)+b)%26] for a,b in zip(txt,lst))

