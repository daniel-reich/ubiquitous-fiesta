
def partially_hide(phrase):
  return ' '.join([i[0]+(len(i)-2)*'-'+i[-1] if len(i)>2 else i for i in phrase.split()])

