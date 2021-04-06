
def shhh(txt):
  if len(txt) > 0:
    new_str = txt[0].upper() + txt[1:].lower()
    return '"' + new_str+'"' + ','+ ' whispered Edabit.'
  else:
    return '"", whispered Edabit.'

