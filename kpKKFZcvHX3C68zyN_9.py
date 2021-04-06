
def swap_cards(n1, n2):
  sn1 = [a for a in str(n1)]
  sn2 = [a for a in str(n2)]
  sn1min = min(sn1)
  pmin = sn1.index(min(sn1))
  sn1[pmin] = sn2[0]
  sn2[0] = sn1min
  if n1%11 != 0:
    return int(''.join(sn1)) > int(''.join(sn2))
  return int(str(n2)[0] + str(n1)[1]) > int(str(n1)[0] + str(n2)[1])

