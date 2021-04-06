
def monkey_talk(txt):
  return ' '.join('Eek' if i[0].lower() in 'aeiou' else 'Ook' for i in txt.split()).capitalize()+'.'

