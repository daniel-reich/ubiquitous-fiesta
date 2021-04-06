
def tweak_letters(txt, lst):
  return ''.join(
    chr(((ord(i) - 97 + j) % 26) + 97) 
    for i, j in zip(txt, lst)
  )

