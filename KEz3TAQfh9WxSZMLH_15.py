
def count_all(txt):
  return {'LETTERS':len([i for i in txt if i.isalpha()]) ,'DIGITS':len([i for i in txt if i.isdigit()]) }

