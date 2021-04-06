
def keyboard_shortcut(txt):
  if 'Ctrl + C' not in txt: return ' '.join(map(str.strip, txt.split('Ctrl + V')))
  else:
    ntoks, out, copied = txt.replace('Ctrl + C', '|').replace('Ctrl + V', '\\').split(), str(), None
    for tok in ntoks:
      if tok not in ('\\', '|'): out += tok + ' '
      elif tok == '|': copied = out
      elif tok == '\\' and copied: out += copied
  return out[:-1]

