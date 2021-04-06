
def shhh(txt):
  if txt:
    return '"{}{}", whispered Edabit.'.format(txt[0].upper(), txt[1:].lower())
  return '"", whispered Edabit.'

