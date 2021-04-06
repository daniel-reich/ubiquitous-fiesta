
def is_icecream_sandwich(txt):
  if len(txt) < 3:
    return False
  count1 = []
  count2 = []
  for i in range(len(txt)//2):
    if txt[i] == txt[i+1]:
      count1.append(txt[i])
    else:
      break
  rev = txt[::-1]
  for i in range(len(rev)//2):
    if rev[i] == rev[i+1]:
      count2.append(txt[i])
    else:
      break
  if txt[int(len(txt)/2)] == txt[0]:
    return False
  chrs = list(txt)
  un = set(chrs)
  if len(un) > 2:
    return False
  if count1 == count2:
    return True
  else:
    return False

