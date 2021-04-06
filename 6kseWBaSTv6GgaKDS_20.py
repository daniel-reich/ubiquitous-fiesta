
def next_letters(s):
  if len(s) == 0:
    return "A"
  pos = len(s) - 1
  end = False
  erg = []
  while pos >= 0:
    if not end:
      if s[pos] != "Z":
        neu = chr(ord(s[pos] ) + 1)
        erg.append(neu)
        end = True
      elif pos == 0:
        erg.append("AA")
        end = False
      else:
        erg.append("A")
    else:
      erg.append(s[pos])
    pos -= 1
  erg.reverse()
  return ''.join(erg)

