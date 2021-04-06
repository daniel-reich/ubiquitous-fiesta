
def monkey_talk(txt):
  res = []
  for i in txt.lower().split():
    res.append('eek' if i[0] in 'aeiou' else 'ook')
  return ' '.join(res).capitalize() + '.'

