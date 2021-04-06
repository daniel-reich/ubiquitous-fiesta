
def missing_letter(lst):
  startnum = ord(lst[0])
  for i in range(startnum,len(lst)+startnum):
    if i > 0:
      if lst[i-startnum] != chr(i): return chr(i)

