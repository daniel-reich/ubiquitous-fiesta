
def switcheroo(txt):
  copy=''.join(i if i.isalpha() else '@' for i in txt).replace('nts@','#').replace('nce@','nts@').replace('#','nce@')
  return ''.join(copy[i] if copy[i].isalpha() else txt[i] for i in range(len(txt)))

