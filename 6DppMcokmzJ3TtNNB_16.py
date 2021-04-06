
def true_alphabetic(txt):
  ch, length, alph = sorted(i for i in txt if i.isalpha()), [len(i) for i in txt.split()], []
  for i in length:
    alph.append(''.join(ch[:i]))
    ch = ch[i:]
  return ' '.join(alph)

