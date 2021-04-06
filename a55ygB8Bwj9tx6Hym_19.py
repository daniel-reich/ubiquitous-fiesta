
def steps_to_convert(txt):
  count_upper = 0
  count_lower = 0
  if txt == '':
    return 0
  else:
    for x in txt:
      if x.islower():
        count_lower += 1
      elif x.isupper():
        count_upper += 1
    if count_lower >= count_upper:
      return count_upper
    elif count_upper > count_lower:
      return count_lower

