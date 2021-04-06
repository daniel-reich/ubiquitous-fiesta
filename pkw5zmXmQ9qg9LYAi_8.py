
def space_message(txt):
  
  while '[' in txt:
    si = len(txt) -1 -txt[::-1].index('[')
    ei = txt[si:].index(']') + si
​
    stxt = txt[si+1: ei]
    txt = txt.replace(txt[si: ei+1], int(stxt[0]) * stxt[1:])
​
  return txt

