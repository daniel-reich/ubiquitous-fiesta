
def find_longest(sentence):
  aa = sentence.split(" ")
  s = "" 
  su =  ""
  bb = list()
  for x in aa:
    s = x.lower()
    for y in s:
      if  97 <= ord(y) <= 123:
        su += y
      else:
        break
    bb.append(su)
    su = " "
  ll = [len(x) for x in bb]
  return bb[ll.index(max(ll))].lstrip()

