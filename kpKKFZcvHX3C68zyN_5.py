
def swap_cards(n1, n2):
  minvalue = min(list([int(x) for x in str(n1)]))
  minindex = str(n1).index(str(minvalue))
  if minindex == 0:
    return int(str(n2)[0] + str(n1)[1]) > int(str(n1)[0] + str(n2)[1])
  else:
    return int(str(n1)[0] + str(n2)[0]) > int(str(n1)[1] + str(n2)[1])

