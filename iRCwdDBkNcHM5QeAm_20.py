
def card_hide(card):
# erg=[]
# for x in range(0,len(card)):
#   if (x <(len(card)-4)):
#     erg.append('*')
#   else:
#     erg.append(card[x])
# return ("".join(erg))
  s = len(card)
  return "".join(['*' if x <s-4 else card[x] for x in range(0,s)])

