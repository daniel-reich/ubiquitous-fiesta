
def kaprekar(num):
  if num == 6174:
    return 0
  else:
    ascending = str(num)
    descending = str(num)
    if len(ascending) < 4:
      ascending += (4-len(ascending)) * "0"
    if len(descending) < 4:
      descending += (4-len(descending)) * "0"
    ascending = "".join(sorted(str(ascending)))
    descending = "".join(sorted(str(descending), reverse=True))
    if int(ascending) >= int(descending):
      return 1 + kaprekar(int(ascending) - int(descending))
    else:
      return 1 + kaprekar(int(descending) - int(ascending))

