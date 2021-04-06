
def monkey_talk(txt):
  return ' '.join(['eek' if x[0].lower() in 'aeiou' else 'ook' \
  for x in txt.split()]).capitalize()+'.'

