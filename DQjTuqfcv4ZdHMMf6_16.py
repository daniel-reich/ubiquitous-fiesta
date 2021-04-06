
def kaprekar(num):
  if num == 6174:
    return 0
  elif len(str(num)) < 4:
    newnum = str(num*10)
    nextnum = int("".join(sorted(newnum, reverse = True)))-int("".join(sorted(newnum)))
    return 1+kaprekar(nextnum)
  else:
    newnum = str(num)
    nextnum = int("".join(sorted(newnum, reverse = True)))-int("".join(sorted(newnum)))
    return 1+kaprekar(nextnum)

