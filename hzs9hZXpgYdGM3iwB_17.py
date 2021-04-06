
import itertools as it
def alternating_caps(txt):
  t   = txt.replace(' ', '')
  alt = [
    l for z in it.zip_longest(
      t[::2].upper(), t[1::2].lower(), fillvalue=''
    ) for l in z
  ]
  return ''.join(c if c == ' ' else alt.pop(0) for c in txt)

