
def monkey_talk(txt):
  def monkify(words):
    tr = []
    for word in words:
      if word[0] in 'aeiouAEIOU':
        tr.append('eek')
      else:
        tr.append('ook')
    return ' '.join(tr)
  
  return monkify(txt.split()).capitalize() + '.'

