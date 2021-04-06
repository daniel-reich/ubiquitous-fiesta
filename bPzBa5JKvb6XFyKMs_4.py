
d = {
'7':21,
'6':18,
'A':16,
'2':12,
'3':13,
'4':14,
'5':15,
'J':10,
'Q':10,
'K':10,
}
def conv(str, deck):
  return sorted(d[x[0]] for x in filter(lambda x: x[1] == str, deck))[-1]
​
def get_primiera_score(deck):
  if any(x not in ''.join(deck) for x in 'dhcs'): return False
  return sum(conv(x, deck) for x in 'dhcs')

