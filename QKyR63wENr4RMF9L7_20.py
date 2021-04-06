
def fix(num):
  n = num + 26 if num < 97 else num - 26 if num > 122 else num
  return chr(n)
  
def tweak_letters(txt, lst):
  return ''.join(fix(ord(ch) + i) for ch, i in zip(txt,lst))

