
def shhh(txt):
  try:
    return '"' + txt.lower()[0].upper() + txt.lower()[1:] +'"' + ', whispered Edabit.'
  except:
    return '""' + ', whispered Edabit.'

