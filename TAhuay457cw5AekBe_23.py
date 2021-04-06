
def monkey_talk(txt):
  res = ['eek' if t[0] in 'aeiouAEIOU' else 'ook' for t in txt.split()]
  return ' '.join(res).capitalize()+'.'

