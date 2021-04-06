
def edit_words(lst):
  return [''.join(reversed(x.upper()[0:len(x)//2] + '-' + x.upper()[len(x)//2:])) for x in lst]

